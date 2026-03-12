import React, { useState } from "react";
import axios from "axios";

export default function Recommendations() {

  const [location, setLocation] = useState("");
  const [category, setCategory] = useState("");
  const [season, setSeason] = useState("");
  const [duration, setDuration] = useState(1);
  const [itinerary, setItinerary] = useState([]);
  const [error, setError] = useState("");

  const fetchItinerary = async () => {
    try {

      const res = await axios.post("http://127.0.0.1:8000/recommendations", {
        location: location,
        category: category,
        season: season,
        duration: Number(duration)
      });

      console.log(res.data);

      if (res.data.itinerary) {
        setItinerary(res.data.itinerary);
        setError("");
      } else {
        setError("No itinerary found");
        setItinerary([]);
      }

    } catch (err) {
      console.error(err);
      setError("Failed to fetch itinerary");
      setItinerary([]);
    }
  };

  return (
    <div style={{ padding: "20px" }}>

      <h2>AI Travel Recommendations</h2>

      <div style={{ marginBottom: "15px" }}>

        <input
          placeholder="Location"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
        />

        <input
          placeholder="Category"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
        />

        <input
          placeholder="Season"
          value={season}
          onChange={(e) => setSeason(e.target.value)}
        />

        <input
          type="number"
          value={duration}
          onChange={(e) => setDuration(e.target.value)}
        />

        <button onClick={fetchItinerary}>
          Get Itinerary
        </button>

      </div>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {itinerary.length > 0 &&

        itinerary.map((day, dayIndex) => (

          <div key={dayIndex} style={{ marginBottom: "20px" }}>

            <h3>Day {dayIndex + 1}</h3>

            {day.map((place) => (

              <div
                key={place.id}
                style={{
                  border: "1px solid #ccc",
                  padding: "10px",
                  marginBottom: "10px",
                  borderRadius: "6px"
                }}
              >

                <p><b>Place:</b> {place.name}</p>

                <p><b>City:</b> {place.city}</p>

                <p><b>Category:</b> {place.category}</p>

                <p><b>Rating:</b> ⭐ {place.rating}</p>

                <p><b>Estimated Cost:</b> ₹{place.estimated_cost}</p>

                

              </div>

            ))}

          </div>

        ))

      }

    </div>
  );
}