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


@llm.ai_callable(
    name="show_furniture_images",
    description="Retrieves the furniture based on user input"
)
async def show_furniture_images(
    self,
    furniture: Annotated[
        str, llm.TypeInfo(
            description="Type of furniture",
            choices=furniture
        )
    ],
    tags: Annotated[
        list[str], llm.TypeInfo(
            description="Comma-separated tags to filter furniture",
            choices=tags
        )
    ] = None,
):
    """Called when the user asks to show furniture images based on type and tags."""

    logging.info("Furniture: %s", furniture)
    logging.info("Tags: %s", tags)

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

    if not images:
        return f"Sorry, I couldn't find any {furniture} in the catalog."

    if tags:
        tag_list = [tag.strip().lower() for tag in tags]
        filtered_images = []

        for image in images:
            if any(tag in image['tags'] for tag in tag_list):
                filtered_images.append(image)

        if not filtered_images:
            return f"Sorry, I couldn't find any {furniture} with the specified tags."

        images = filtered_images

    payload = json.dumps({
        "type": "furniture_images",
        "data": images
    })

    # Get the participant identities from the room context
    participant_identity2 = self.room.remote_participants
    for identity, participant in participant_identity2.items():
        identity = participant.identity
        participant_identity2 = identity

    # Attempt to publish the data to the LiveKit room
    try:
        await self.room.local_participant.publish_data(
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
async def get_greet_fun(self):
    """Greet the user in Spanish."""
    print("RUNNING GREET")
    return "Hola amigo"


@llm.ai_callable()
async def get_top_songs(self):
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
    def __init__(self, room, functions=None):
        self.room = room
        self.functions = functions
        self._bind_selected_functions()
        super().__init__()

    def _bind_selected_functions(self):
        """Dynamically bind selected functions to the class and register them."""
        available_functions = {
            "show_furniture_images": show_furniture_images,
            "get_greet_fun": get_greet_fun,
            "get_top_songs": get_top_songs,
        }

        for func_name in self.functions:
            print(f"Attempting to bind function: {func_name}")
            func = available_functions.get(func_name)
            if func:
                bound_func = func
                setattr(DynamicAssistantFnc, func_name, bound_func)


# Entry point for the job
async def entrypoint(ctx: JobContext):
    initial_ctx = llm.ChatContext().append(
        role="system",
        text=""
        # text=(
        #     "You are a highly knowledgeable and friendly interior design assistant specializing in creating kid-friendly room designs. Your goal is to help parents and guardians design functional, fun, and visually appealing rooms tailored to their children's age, interests, and needs. Your advice should: Emphasize safety, durability, and easy maintenance. Include creative ideas for storage, play, study, and sleep areas. Suggest colors, themes, furniture, and layouts that stimulate creativity and comfort. Provide tips on space optimization for small or shared rooms. Adapt suggestions based on age group (toddlers, school-aged kids, or teenagers). Encourage input from the kids, ensuring the design reflects their personalities and interests. Start by understanding the room's dimensions, current layout, the child’s preferences, and any constraints (e.g., budget, rental restrictions). Offer practical solutions and customizable ideas that can grow with the child. Ask the questions about room size, type of bed, overall theme, wall color, desks needed, wardrobes style and budget. Ask questions one by one on the topics. Try to keep your response brief under 30 words and do not use numbering in it. Try to sound conversational"
        #     "Do not say anything while waiting for the function call to complete."
        #     "If user share any tags then Describe the user-selected product keep it short and clear"
        #     """If the user's requested tag is not found in the predefined list of tags, notify the user that the specific type of furniture could not be located. Then proceed to make the function call with the provided furniture name, setting the tags to None
        #     tags=(
        #         "sofa", "leather", "red", "modern", "comfortable", "fabric", "green", "classic", "elegant",
        #         "yellow", "7-seater", "chaise-longue", "blue", "5-seater", "bed", "wood", "brown",
        #         "king-size", "luxury", "super-double-size", "extra-storage", "gray", "metal-legs",
        #         "leather-lining", "white", "loft-bed", "desk-with-storage", "space-saving", "slatted-bed-base", "bed-with-storage", "guard-rail", "bed-with-underbed-storage",
        #         "extendable-bed", "dining-table", "marble-surface", "gold-base", "white-marble", "spacious",
        #         "accommodates-6-people", "metal-base", "black-marble", "elegant", "timeless-style",
        #         "extendable-table", "particleboard", "oak-veneer", "steel-frame", "solid-wood", "ash-veneer",
        #         "solid-pine",  "classic-look", "black-and-dark-brown", "white-finish", "beige-seats",
        #         "family-dining", "outdoor-table-and-chairs", "aluminium", "steel", "dark-green", "beige-cushions",
        #         "desk", "fibreboard", "acrylic-paint", "bamboo", "sustainable", "plywood", "oak-veneer",
        #         "gaming-desk", "wardrobe", "", "fibreboard", "printed-acrylic-paint", "sliding-doors", "recycled-materials", "epoxy-coating", "soft-closing-hinge",
        #         "copper-plated-hinge", "acetal-plastic", "adjustable-leg", "polypropylene-plastic", "clear-lacquer",
        #         "blackboard-surface", "adjustable-clothes-rail", "wire-basket", "solid-pine", "stain",
        #         "plastic-foil", "synthetic-rubber", "melamine-foil", "plastic-edging", "anodized",
        #         "reinforced-polyamide-plastic", "dining-chair", "beige", "pvc-material", "stainless-steel-legs",
        #         "black", "bouclé-fabric", "metal-legs", "ergonomic"
        #     )"""
        # ),
    )

    logger.info(f"Connecting to room {ctx.room.name}")
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    # selected_functions = ["get_top_songs",
    #                       "get_greet_fun"]
    selected_functions = ["get_top_songs", "show_furniture_images"]
    fnc_ctx = DynamicAssistantFnc(room=ctx.room,
                                  functions=selected_functions)

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


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
