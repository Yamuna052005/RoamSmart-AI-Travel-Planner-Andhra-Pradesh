import axios from "axios";

// FastAPI Backend
const API_BASE = "http://localhost:8000";

// Unsplash Access Key
const UNSPLASH_KEY = "";

// -----------------------------
// Voice Assistant
// -----------------------------
export const askAssistant = (query) => {
  return axios.post(`${API_BASE}/assistant`, { query });
};

// -----------------------------
// Weather Service
// -----------------------------
export const getWeather = (city) => {
  return axios.get(`${API_BASE}/weather?city=${city}`);
};

// -----------------------------
// Recommendations Service
// -----------------------------
export const getRecommendations = (params) => {
  return axios.post(`${API_BASE}/recommendations`, params);
};

// -----------------------------
// Cost Predictor Service
// -----------------------------
export const predictCost = async (form) => {
  return axios.get(`${API_BASE}/predict_cost`, {
    params: {
      rating: form.rating,
      category: form.category,
      city: form.city,
      distance: form.distance,
      season: form.season,
    },
  });
};

// -----------------------------
// Unsplash Image Service
// -----------------------------
export const getPlaceImage = async (place) => {
  try {
    const res = await axios.get(
      `https://api.unsplash.com/photos/random`,
      {
        params: {
          query: place,
          orientation: "landscape",
        },
        headers: {
          Authorization: `Client-ID ${UNSPLASH_KEY}`,
        },
      }
    );

    return res.data.urls.regular;
  } catch (error) {
    console.error("Unsplash image fetch error:", error);
    return "";
  }
};