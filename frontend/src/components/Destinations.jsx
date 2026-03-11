import React, { useEffect, useState } from "react";
import axios from "axios";
import { getPlaceImage } from "../services/api";

export default function Destinations() {
  const [destinations, setDestinations] = useState([]);

  useEffect(() => {
    const fetchDestinations = async () => {
      try {
        const res = await axios.get("http://127.0.0.1:8000/destinations");

        // Fetch Unsplash image for each destination
        const destinationsWithImages = await Promise.all(
          res.data.map(async (destination) => {
            const image = await getPlaceImage(destination.name || destination.city);
            return { ...destination, image_url: image };
          })
        );

        setDestinations(destinationsWithImages);
      } catch (err) {
        console.error("Failed to fetch destinations", err);
      }
    };

    fetchDestinations();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Destinations</h2>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fill, minmax(250px, 1fr))",
          gap: "20px",
        }}
      >
        {destinations.map((destination) => (
          <div
            key={destination.id}
            style={{
              border: "1px solid #ddd",
              borderRadius: "8px",
              overflow: "hidden",
              boxShadow: "0 2px 6px rgba(0,0,0,0.1)",
              backgroundColor: "#fff",
            }}
          >
            {destination.image_url && (
              <img
                src={destination.image_url}
                alt={destination.name}
                style={{
                  width: "100%",
                  height: "180px",
                  objectFit: "cover",
                }}
              />
            )}

            <div style={{ padding: "10px" }}>
              <h3 style={{ margin: "0 0 10px" }}>{destination.name}</h3>
              <p><strong>City:</strong> {destination.city}</p>
              <p><strong>Category:</strong> {destination.category}</p>
              <p><strong>Rating:</strong> ⭐ {destination.rating}</p>
              <p><strong>Estimated Cost:</strong> ₹{destination.estimated_cost}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}