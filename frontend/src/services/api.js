import axios from "axios";

const API_BASE = "http://localhost:8000";
const UNSPLASH_KEY = "guVHoYWIAmdvBtj3wqAZDgEUnYCm2HeqJ7VkyDpvybc"; // keep your key

// ---------------- Voice Assistant ----------------
export const askAssistant = (query) => {
  return axios.post(`${API_BASE}/assistant`, { query });
};

// ---------------- Weather Service ----------------
export const getWeather = (city) => {
  return axios.get(`${API_BASE}/weather?city=${city}`);
};

// ---------------- Recommendations Service ----------------
export const getRecommendations = (params) => {
  return axios.post(`${API_BASE}/recommendations`, params);
};

// ---------------- Cost Predictor ----------------
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

// ---------------- Unsplash Image ----------------
// Uses category_keyword for relevance and fetches multiple images
export const getPlaceImage = async (categoryKeyword) => {
  try {
    const res = await axios.get("https://api.unsplash.com/search/photos", {
      params: {
        query: categoryKeyword, // use category_keyword from DB
        per_page: 5,            // fetch 5 images to pick randomly
        orientation: "landscape",
      },
      headers: {
        Authorization: `Client-ID ${UNSPLASH_KEY}`,
      },
    });

    if (res.data.results.length > 0) {
      // Pick a random image from the fetched results
      const randomIndex = Math.floor(Math.random() * res.data.results.length);
      return res.data.results[randomIndex].urls.regular;
    }

    // fallback generic travel image
    return "https://source.unsplash.com/400x300/?travel";
  } catch (error) {
    console.error("Unsplash fetch error:", error.message);
    return "https://source.unsplash.com/400x300/?travel";
  }
};