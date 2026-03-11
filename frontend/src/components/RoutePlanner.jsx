import React, { useState } from "react";
import axios from "axios";

export default function RoutePlanner() {
  const [destinations, setDestinations] = useState([]);
  const [routeData, setRouteData] = useState(null);

  const handleAdd = () => {
    setDestinations([...destinations, { name: "" }]);
  };

  const handleChange = (i, value) => {
    const updated = [...destinations];
    updated[i].name = value;
    setDestinations(updated);
  };

  const handleSubmit = async () => {
    try {
      // Transform destinations into ["Visakhapatnam", "Tirupati"]
      const places = destinations.map((d) => d.name).filter((n) => n.trim() !== "");
      const res = await axios.post("http://127.0.0.1:8000/itinerary/route", {
        places: places,
      });
      setRouteData(res.data);
    } catch (err) {
      console.error("Error fetching route:", err);
      setRouteData(null);
    }
  };

  return (
    <div>
      <h2>Route Planner</h2>
      {destinations.map((d, i) => (
        <div key={i}>
          <input
            placeholder="Enter Destination Name"
            value={d.name}
            onChange={(e) => handleChange(i, e.target.value)}
          />
        </div>
      ))}
      <button onClick={handleAdd}>Add Destination</button>
      <button onClick={handleSubmit}>Optimize Route</button>

      {routeData && (
        <div style={{ marginTop: "20px" }}>
          <h3>Optimized Route</h3>
          <ol>
            {routeData.optimized_route?.map((r, i) => (
              <li key={i}>
                {r.order}. {r.name} ({r.latitude}, {r.longitude})
              </li>
            ))}
          </ol>

          <h3>Travel Instructions</h3>
          <ul>
            {routeData.instructions?.map((inst, i) => (
              <li key={i}>
                {inst.text} — {(inst.distance_m / 1000).toFixed(1)} km,{" "}
                {(inst.time_ms / 60000).toFixed(0)} min
              </li>
            ))}
          </ul>

          <h4>Summary</h4>
          <p>Total Distance: {routeData.total_distance_km} km</p>
          <p>Estimated Travel Time: {routeData.estimated_travel_time_min} minutes</p>
        </div>
      )}
    </div>
  );
}