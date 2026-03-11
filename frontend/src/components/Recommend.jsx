import React, { useState } from "react";
import { getRecommendations } from "../services/api";

export default function Recommendations() {
  const [location, setLocation] = useState("");
  const [category, setCategory] = useState("");
  const [season, setSeason] = useState("");
  const [duration, setDuration] = useState(1);
  const [itinerary, setItinerary] = useState(null);

  const handleSubmit = async () => {
    try {
      const res = await getRecommendations({
        location,
        category,
        season,
        duration
      });
      setItinerary(res.data);
    } catch {
      setItinerary({ error: "Failed to fetch recommendations" });
    }
  };

  return (
    <div>
      <h2>AI Recommendations</h2>
      <input
        placeholder="Enter location..."
        value={location}
        onChange={(e) => setLocation(e.target.value)}
      />
      <input
        placeholder="Enter category..."
        value={category}
        onChange={(e) => setCategory(e.target.value)}
      />
      <input
        placeholder="Enter season..."
        value={season}
        onChange={(e) => setSeason(e.target.value)}
      />
      <input
        type="number"
        placeholder="Duration (days)"
        value={duration}
        onChange={(e) => setDuration(Number(e.target.value))}
      />
      <button onClick={handleSubmit}>Get Itinerary</button>

      {itinerary && !itinerary.error && !itinerary.message && (
        <div style={{ marginTop: "1rem", display: "grid", gap: "1rem" }}>
          <h3>Your Itinerary</h3>
          {itinerary.map((place, index) => (
            <div
              key={index}
              style={{
                background: "#f9f9f9",
                border: "1px solid #ddd",
                borderRadius: "8px",
                padding: "1rem",
                boxShadow: "0 2px 6px rgba(0,0,0,0.1)"
              }}
            >
              <h4>Day {index + 1}: {place.name}</h4>
              <p><strong>City:</strong> {place.city}</p>
              <p><strong>Category:</strong> {place.category}</p>
              <p><strong>Rating:</strong> {place.rating}</p>
              <p><strong>Estimated Cost:</strong> ₹{place.estimated_cost}</p>
              <p><strong>Season:</strong> {place.season}</p>
              <p><strong>Coordinates:</strong> {place.latitude}, {place.longitude}</p>
            </div>
          ))}
        </div>
      )}

      {itinerary?.message && <p>{itinerary.message}</p>}
      {itinerary?.error && <p>{itinerary.error}</p>}
    </div>
  );
}