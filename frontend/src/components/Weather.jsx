import React, { useState } from "react";
import { getWeather } from "../services/api";

export default function Weather() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null);

  const handleSubmit = async () => {
    try {
      const res = await getWeather(city);
      setWeather(res.data);
    } catch {
      setWeather({ error: "Failed to fetch weather" });
    }
  };

  return (
    <div>
      <h2>Weather</h2>
      <input
        placeholder="Enter city..."
        value={city}
        onChange={(e) => setCity(e.target.value)}
      />
      <button onClick={handleSubmit}>Get Weather</button>

      {weather && !weather.error && (
        <div>
          <p>City: {weather.city}</p>
          <p>Temperature: {weather.temperature}°C</p>
          <p>Humidity: {weather.humidity}%</p>
          <p>Condition: {weather.description}</p>
          <p>Wind Speed: {weather.wind_speed} m/s</p>
        </div>
      )}

      {weather?.error && <p>{weather.error}</p>}
    </div>
  );
}
