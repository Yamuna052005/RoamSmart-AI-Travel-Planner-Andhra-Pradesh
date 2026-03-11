import React, { useState } from "react";
import { predictCost } from "../services/api";

export default function CostPredict() {
  const [form, setForm] = useState({
    rating: 4.4,
    category: "Temple",
    city: "Tirupati",
    distance: 500,
    season: "summer",
  });
  const [result, setResult] = useState(null);

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async () => {
    try {
      const res = await predictCost(form);
      setResult(res.data.predicted_cost);
    } catch (err) {
      console.error("Error fetching cost:", err);
      setResult("Failed to fetch cost prediction");
    }
  };

  return (
    <div className="section-bg cost"> 
      <h2>Travel Cost Prediction</h2>
      <input
        name="rating"
        value={form.rating}
        onChange={handleChange}
        placeholder="Rating"
      />
      <input
        name="category"
        value={form.category}
        onChange={handleChange}
        placeholder="Category"
      />
      <input
        name="city"
        value={form.city}
        onChange={handleChange}
        placeholder="City"
      />
      <input
        name="distance"
        value={form.distance}
        onChange={handleChange}
        placeholder="Distance (km)"
      />
      <input
        name="season"
        value={form.season}
        onChange={handleChange}
        placeholder="Season"
      />
      <button onClick={handleSubmit}>Predict Cost</button>

      {result && (
        <p>
          Predicted Cost:{" "}
          {typeof result === "number" ? `₹${result.toFixed(2)}` : result}
        </p>
      )}
    </div>
  );
}