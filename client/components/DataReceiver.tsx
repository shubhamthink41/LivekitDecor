import { useState } from "react";
import Image from "next/image";
import { useDataChannel } from "@livekit/components-react";
import { RoomActions } from "@/app/page";

function DataReceiver() {
  const [imageLinks, setImageLinks] = useState<
    { url: string; tags: string[] }[]
  >([]);
  const [selectedTags, setSelectedTags] = useState<string[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  useDataChannel("furniture_images", (msg) => {
    console.log("Message received:", msg);

    try {
      setLoading(true);
      const data = JSON.parse(new TextDecoder().decode(msg.payload));

      if (data.type === "furniture_images" && Array.isArray(data.data)) {
        const links = data.data.map(
          (item: { image_url: string; tags: string[] }) => ({
            url: item.image_url,
            tags: item.tags,
          })
        );
        setImageLinks(links);
        setLoading(false);
      } else {
        console.warn("Invalid data format:", data);
        setError("Invalid image data format received.");
        setLoading(false);
      }
    } catch (err) {
      console.error("Failed to parse message payload:", err);
      setError("An error occurred while processing the data.");
      setLoading(false);
    }
  });

  const handleImageSelect = (image: { url: string; tags: string[] }) => {
    console.log("Selected Image Tags:", image.tags);
    setImageLinks([image]); 
    setSelectedTags(image.tags);
  };

  return (
    
    <div className="w-full h-full">
      {loading ? (
        <p className="text-gray-600 text-center">Loading images...</p>
      ) : error ? (
        <p className="text-red-600 text-center">{error}</p>
      ) : imageLinks.length > 0 ? (
        <div className="grid grid-cols-2 gap-4">
          {imageLinks.map((image, index) => (
            <div key={index}>
              <Image
                src={image.url}
                alt={`Option ${index + 1}`}
                className="object-cover w-full p-4  hover:opacity-70  h-full cursor-pointer transition-transform"
                width={300}
                height={300}
                onClick={() => handleImageSelect(image)}
              />
            </div>
          ))}
        </div>
      ) : (
        <p className="text-gray-600 text-center">
          No images available for selection.
        </p>
      )}
      {selectedTags.length > 0 && <RoomActions selectedTags={selectedTags} />}
    </div>
  );
}

export default DataReceiver;
