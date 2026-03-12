import React, { useState } from "react";
import axios from "axios";

export default function Itinerary() {
  const [city, setCity] = useState("");
  const [days, setDays] = useState(2);
  const [preference, setPreference] = useState("");
  const [season, setSeason] = useState("");
  const [itinerary, setItinerary] = useState([]);
  const [error, setError] = useState("");

  const handleSubmit = async () => {
    try {
      const res = await axios.get(`http://127.0.0.1:8000/itinerary/${city}`, {
        params: { days, preference, season },
      });

      if (!res.data.itinerary) {
        setError("No itinerary found");
        setItinerary([]);
      } else {
        setItinerary(res.data.itinerary);
        setError("");
      }
    } catch (err) {
      console.error(err);
      setError("Failed to fetch itinerary");
      setItinerary([]);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>AI Itinerary Planner</h2>

      <div style={{ marginBottom: "15px" }}>
        <input
          placeholder="Enter city..."
          value={city}
          onChange={(e) => setCity(e.target.value)}
          style={{ marginRight: "5px" }}
        />
        <input
          type="number"
          placeholder="Days"
          value={days}
          onChange={(e) => setDays(Number(e.target.value))}
          style={{ width: "60px", marginRight: "5px" }}
        />
        <input
          placeholder="Preference"
          value={preference}
          onChange={(e) => setPreference(e.target.value)}
          style={{ marginRight: "5px" }}
        />
        <input
          placeholder="Season"
          value={season}
          onChange={(e) => setSeason(e.target.value)}
          style={{ marginRight: "5px" }}
        />
        <button onClick={handleSubmit}>Get Itinerary</button>
      </div>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {itinerary.length > 0 &&
        itinerary.map((day, index) => (
          <div key={index} style={{ marginBottom: "20px" }}>
            <h3>Day {index + 1}</h3>
            {day.map((place) => (
              <div
                key={place.id}
                style={{
                  border: "1px solid #ddd",
                  borderRadius: "8px",
                  padding: "10px",
                  marginBottom: "10px",
                  backgroundColor: "#f9f9f9",
                }}
              >
                <strong>{place.name}</strong> ({place.category})<br />
                City: {place.city} | Rating: ⭐ {place.rating} | Cost: ₹{place.estimated_cost}<br />
                Distance: {place.distance ? place.distance.toFixed(1) : 0} km
              </div>
            ))}
          </div>
        ))}
    </div>
  );
}