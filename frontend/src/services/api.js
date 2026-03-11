import axios from "axios";

const API_BASE = "http://localhost:8000";

const UNSPLASH_KEY = "acCXdTwPzsmfyGFCQsEcsQCZJUX4xPkuKvz8VAeQ";

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

// Cost Predictor
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

// Unsplash Image
export const getPlaceImage = async (place) => {
  try {
    const res = await axios.get(
      "https://api.unsplash.com/search/photos",
      {
        params: {
          query: place,
          per_page: 1
        },
        headers: {
          Authorization: `Client-ID ${UNSPLASH_KEY}`
        }
      }
    );

    if (res.data.results.length > 0) {
      return res.data.results[0].urls.regular;
    }

    return "https://source.unsplash.com/400x300/?travel";
  } catch (error) {
    console.error("Unsplash image fetch error:", error);
    return "https://source.unsplash.com/400x300/?travel";
  }
};