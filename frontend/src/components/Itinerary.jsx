import React, { useState } from "react";
import axios from "axios";

export default function Itinerary() {
  const [city, setCity] = useState("");
  const [days, setDays] = useState(2);
  const [preference, setPreference] = useState("");
  const [season, setSeason] = useState("");
  const [itinerary, setItinerary] = useState(null);

  const handleSubmit = async () => {
    try {
      const res = await axios.get(`http://localhost:8000/itinerary/${city}`, {
        params: { days, preference, season }
      });
      setItinerary(res.data);
    } catch {
      setItinerary({ error: "Failed to fetch itinerary" });
    }
  };

  return (
    <div>
      <h2>AI Itinerary Planner</h2>
      <input
        placeholder="Enter city..."
        value={city}
        onChange={(e) => setCity(e.target.value)}
      />
      <input
        type="number"
        placeholder="Days"
        value={days}
        onChange={(e) => setDays(Number(e.target.value))}
      />
      <input
        placeholder="Preference (temple, nature...)"
        value={preference}
        onChange={(e) => setPreference(e.target.value)}
      />
      <input
        placeholder="Season (summer, winter...)"
        value={season}
        onChange={(e) => setSeason(e.target.value)}
      />
      <button onClick={handleSubmit}>Get Itinerary</button>

      {itinerary?.error && <p>{itinerary.error}</p>}

      {itinerary?.itinerary && (
        <div style={{ marginTop: "1rem" }}>
          <h3>{itinerary.city} Itinerary</h3>
          {itinerary.itinerary.map((day) => (
            <div key={day.day} style={{ marginBottom: "1rem" }}>
              <h4>Day {day.day}</h4>
              {day.places.map((place) => (
                <div key={place.id} style={{ marginLeft: "1rem" }}>
                  <p><strong>{place.name}</strong> ({place.category})</p>
                  <p>Rating: {place.rating} | Cost: ₹{place.estimated_cost}</p>
                  <p>Distance: {place.distance ? place.distance.toFixed(1) : 0} km</p>
                  <img
                    src={place.image_url}
                    alt={place.name}
                    style={{ width: "200px", borderRadius: "8px" }}
                  />
                </div>
              ))}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}