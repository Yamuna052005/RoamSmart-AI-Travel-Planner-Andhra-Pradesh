import React, { useEffect, useState } from "react";
import axios from "axios";
import { getPlaceImage } from "../api";

const API_BASE = "http://localhost:8000";

const Destinations = () => {

  const [places, setPlaces] = useState([]);
  const [images, setImages] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {

    const fetchDestinations = async () => {
      try {

        const res = await axios.get(`${API_BASE}/destinations`);
        const placesList = res.data;
        setPlaces(placesList);

        const imagePromises = placesList.map(async (place) => {
          try {
            const img = await getPlaceImage(place.name);
            return { name: place.name, url: img };
          } catch {
            return {
              name: place.name,
              url: "https://source.unsplash.com/400x300/?travel"
            };
          }
        });

        const results = await Promise.all(imagePromises);

        const imageMap = {};
        results.forEach((item) => {
          imageMap[item.name] = item.url;
        });

        setImages(imageMap);
        setLoading(false);

      } catch (error) {
        console.error("Error fetching destinations:", error);
        setLoading(false);
      }
    };

    fetchDestinations();

  }, []);

  return (
    <div style={{ padding: "30px" }}>

      <h1>Destinations</h1>

      {loading && <p>Loading destinations...</p>}

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(250px,1fr))",
          gap: "20px",
          marginTop: "20px",
        }}
      >

        {places.map((place, index) => (

          <div
            key={index}
            style={{
              borderRadius: "10px",
              overflow: "hidden",
              boxShadow: "0 4px 10px rgba(0,0,0,0.1)",
              background: "white",
            }}
          >

            <img
              src={
                images[place.name] ||
                "https://source.unsplash.com/400x300/?travel"
              }
              alt={place.name}
              style={{
                width: "100%",
                height: "180px",
                objectFit: "cover",
              }}
            />

            <div style={{ padding: "15px" }}>

              <h3>{place.name}</h3>

              <p><b>City:</b> {place.city}</p>

              <p><b>Category:</b> {place.category}</p>

              <p>⭐ {place.rating}</p>

              <p><b>Estimated Cost:</b> ₹{place.estimated_cost}</p>

            </div>

          </div>

        ))}

      </div>

    </div>
  );
};

export default Destinations;