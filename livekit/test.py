import json
import asyncio
import logging
from dotenv import load_dotenv
from livekit import rtc
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import deepgram, openai, silero
from typing import Annotated
import random
from typing import Annotated
from livekit.agents.pipeline import AgentCallContext
from furniture_catalog import furniture_catalog, tags, furniture


load_dotenv()

logger = logging.getLogger("voice-assistant")


@llm.ai_callable()
async def show_furniture_images(furniture: str, tags: list[str] = None):
    """Fetch and send furniture images based on type and tags."""
    call_ctx = AgentCallContext.get_current()
    filler_messages = [
        f"Let me show you some {furniture} images.",
        f"Here are some {furniture} images for you.",
        f"Let me display the {furniture} images I have."
    ]
    message = random.choice(filler_messages)

    speech_handle = await call_ctx.agent.say(message, add_to_chat_ctx=True) if call_ctx and call_ctx.agent else None
    if speech_handle:
        await speech_handle.join()

    images = furniture_catalog.get(furniture.lower())

    print("IMAGES - ", images)

    if not images:
        return f"Sorry, I couldn't find any {furniture} in the catalog."

    if tags:
        tag_list = [tag.strip().lower() for tag in tags]
        filtered_images = [image for image in images if any(
            tag in image['tags'] for tag in tag_list)]

        if not filtered_images:
            return f"Sorry, I couldn't find any {furniture} with the specified tags."

        images = filtered_images

    payload = json.dumps({
        "type": "furniture_images",
        "data": images
    })

    print("PAYLOAD - ", payload)

    # Assuming a participant is identified here for publishing
    participant_identity2 = "some_participant"

    try:
        await call_ctx.room.local_participant.publish_data(
            payload=payload,
            reliable=True,
            destination_identities=[participant_identity2],
            topic="furniture_images"
        )
        print("Data published successfully to LiveKit")
    except Exception as e:
        print("Error publishing data to LiveKit:", str(e))

    return f"Sending {furniture} images based on your tags."


@llm.ai_callable()
async def get_greet_fun():
    """Greet the user in Spanish."""
    print("RUNNING GREET")
    return "Hola amigo"


@llm.ai_callable()
async def get_top_songs():
    """Get the top 10 latest songs."""
    print("Get the top 10 latest songs. RNS")
    return [
        "1. Blinding Lights - The Weeknd",
        "2. Save Your Tears - The Weeknd",
        "3. Levitating - Dua Lipa feat. DaBaby",
        "4. Good 4 U - Olivia Rodrigo",
        "5. Kiss Me More - Doja Cat feat. SZA",
        "6. Montero (Call Me By Your Name) - Lil Nas X",
        "7. Peaches - Justin Bieber feat. Daniel Caesar, Giveon",
        "8. Industry Baby - Lil Nas X feat. Jack Harlow",
        "9. Stay - The Kid LAROI & Justin Bieber",
        "10. Heat Waves - Glass Animals",
    ]


# Define the DynamicAssistantFnc class
class DynamicAssistantFnc(llm.FunctionContext):
    def __init__(self, room, selected_functions=None):
        super().__init__()
        self.room = room
        self.selected_functions = selected_functions or []
        self._bind_selected_functions()

    def _bind_selected_functions(self):
        """Dynamically bind selected functions to the class and register them."""
        available_functions = {
            "show_furniture_images": show_furniture_images,
            "get_greet_fun": get_greet_fun,
            "get_top_songs": get_top_songs,
        }

        for func_name in self.selected_functions:
            print(f"Attempting to bind function: {func_name}")
            func = available_functions.get(func_name)
            if func:
                # Use the original function without binding to self for registration
                bound_func = func
                setattr(self, func_name, bound_func)

                # Register the function if not already registered
                if func_name not in self.ai_functions:
                    logger.info(f"Registering function: {func_name}")
                    # Register the original function
                    self._register_ai_function(bound_func)
                else:
                    logger.warning(
                        f"Function {func_name} is already registered. Skipping.")


# Entry point for the job
async def entrypoint(ctx: JobContext):
    initial_ctx = llm.ChatContext().append(
        role="system",
        text=(
            "Answer as you wish"
        ),
    )

    logger.info(f"Connecting to room {ctx.room.name}")
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    selected_functions = ["get_top_songs",
                          "get_greet_fun"]  # User-selected functions
    fnc_ctx = DynamicAssistantFnc(
        ctx.room, selected_functions=selected_functions)

    participant = await ctx.wait_for_participant()
    logger.info(
        f"Starting voice assistant for participant {participant.identity}")

    agent = VoiceAssistant(
        vad=silero.VAD.load(),
        stt=deepgram.STT(),
        llm=openai.LLM(model="gpt-4o-mini"),
        tts=openai.TTS(),
        chat_ctx=initial_ctx,
        fnc_ctx=fnc_ctx,
    )

    agent.start(ctx.room, participant)

    async def answer_from_text(txt: str):
        chat_ctx = agent.chat_ctx.copy()
        chat_ctx.append(role="user", text=txt)
        stream = agent.llm.chat(chat_ctx=chat_ctx)
        await agent.say(stream)

    @ctx.room.on('data_received')
    def on_data_received(data_packet):
        raw_data = data_packet.data
        parsed_data = json.loads(raw_data)

        print("Data received from participant:", parsed_data["data"])

        furniture_type = parsed_data["data"]

        asyncio.create_task(answer_from_text(furniture_type))

    await agent.say("Hey! How are you doing?", allow_interruptions=True)


# Run the application
if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
