import axios from "axios";

// Point to your FastAPI backend
const API_BASE = "http://localhost:8000";

// Voice Assistant
export const askAssistant = (query) => {
  return axios.post(`${API_BASE}/assistant`, { query });
};

// Weather Service
export const getWeather = (city) => {
  return axios.get(`${API_BASE}/weather?city=${city}`);
};

// Recommendations Service
export const getRecommendations = (params) => {
  return axios.post(`${API_BASE}/recommendations`, params);
};

// Cost Predictor Service (optional if you use it)
export const predictCost = async (form) => {
  return axios.get("http://127.0.0.1:8000/predict_cost", {
    params: {
      rating: form.rating,
      category: form.category,
      city: form.city,
      distance: form.distance,
      season: form.season,
    },
  });
};
