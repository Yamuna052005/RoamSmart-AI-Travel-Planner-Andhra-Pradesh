# 🌍 RoamSmart – AI Travel Planner for Andhra Pradesh

![Python](https://img.shields.io/badge/Python-3.11-blue)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Machine Learning](https://img.shields.io/badge/AI-ML-orange)
![License](https://img.shields.io/badge/Project-Educational-lightgrey)

RoamSmart is an **AI-powered travel planning platform** designed to help users explore destinations across Andhra Pradesh intelligently.
The system combines **machine learning models, real-time weather data, route optimization, and itinerary generation** to create personalized travel plans.

Instead of manually planning trips, users can receive **automated destination recommendations, cost predictions, and optimized travel itineraries**.

---

# ✨ Features

### 🌍 AI Destination Recommendation

Recommends tourist destinations based on user preferences using machine learning algorithms.

### 💰 Travel Cost Prediction

Predicts approximate travel cost using a trained machine learning model.

### 📅 Smart Itinerary Generator

Automatically generates a structured day-wise travel itinerary.

### 🌤️ Live Weather Information

Displays real-time weather data for selected destinations.

### 🗺️ Route Planner

Optimizes travel routes between multiple locations.

### 🧠 Collaborative Filtering

Suggests destinations using preference similarity between users.

### 🎤 Voice Assistant

Allows users to interact with the system using voice commands.

---

# 📸 Application Screenshots

### 🏠 Home Page  and Destination Recommendation

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/7a16fc2d-f7f2-4e49-a811-bd979cee1a44" />

### 📅 Smart Itinerary Generator

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/97f2e0ee-1046-42e1-9893-74d4abfe026b" />

<img width="1920" height="968" alt="Image" src="https://github.com/user-attachments/assets/fb0ac7a0-bc35-44f8-bebf-1563b1fcfb1a" />

### 💰 Travel Cost Prediction

<img width="1920" height="972" alt="Image" src="https://github.com/user-attachments/assets/2bbdce4e-a5fa-49de-8515-f70fdf0d4bd7" />

### 🗺️ Route Planner

<img width="1920" height="964" alt="Image" src="https://github.com/user-attachments/assets/e1133fd7-da45-47f8-9327-6f9291c32dec" />

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/22544121-8049-4d40-9a74-1e529a7bd11f" />

### 🌤️ Weather Information

<img width="1920" height="974" alt="Image" src="https://github.com/user-attachments/assets/49e1eab3-5550-4c63-90d4-ca2b7bead2e5" />

### 🎤 Voice Assistant

<img width="1920" height="972" alt="Image" src="https://github.com/user-attachments/assets/5f444a4d-a035-4600-bc21-36df33143a7c" />

---

# 🏗️ System Architecture

```id="3o0y5t"
User Interface (React + Vite)
        │
        ▼
REST API Layer (FastAPI)
        │
        ▼
AI & ML Services
 ├── Destination Recommendation
 ├── Cost Prediction Model
 ├── Itinerary Generator
 └── Route Optimization
        │
        ▼
Database (PostgreSQL)
```

The system follows a **modular architecture**, separating frontend UI, backend APIs, machine learning services, and data storage.

---

# 📂 Project Structure

``` id="19uels"
RoamSmart
│
├── backend
│   ├── ai
│   ├── ml_models
│   ├── services
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── seed_full.py
│   └── requirements.txt
│
├── frontend
│   ├── src
│   │   ├── components
│   │   ├── services
│   │   └── App.jsx
│   ├── public
│   ├── package.json
│   └── vite.config.js
│
├── screenshots
│   ├── home.png
│   ├── destinations.png
│   ├── itinerary.png
│   └── weather.png
│
├── README.md
└── .gitignore
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```id="ghd2o1"
git clone https://github.com/YOUR_USERNAME/RoamSmart-AI-Travel-Planner-Andhra-Pradesh.git
```

```id="v0hn79"
cd RoamSmart-AI-Travel-Planner-Andhra-Pradesh
```

---

# 🖥️ Backend Setup

Create a virtual environment:

python -m venv venv


Activate the environment:

Windows:

venv\Scripts\activate


Install dependencies:


pip install -r backend/requirements.txt


Run the backend server:

```id="cn9vth"
uvicorn backend.main:app --reload
```

Backend runs at:

```id="7rq3wi"
http://localhost:8000
```

---

# 💻 Frontend Setup

Navigate to frontend folder:

```id="uh79hx"
cd frontend
```

Install dependencies:

```id="s2r87f"
npm install
```

Start frontend development server:

```id="l4sdj3"
npm run dev
```

Frontend runs at:

```id="fqqod8"
http://localhost:5173
```

---

# 🧠 Machine Learning Modules

| Module                  | Description                                   |
| ----------------------- | --------------------------------------------- |
| Destination Recommender | Suggests places based on user interests       |
| Cost Predictor          | Estimates travel expenses                     |
| Collaborative Filtering | Recommends destinations using user similarity |
| Route Optimization      | Finds efficient travel paths                  |
| Itinerary Generator     | Creates structured day-wise travel plans      |

---

# 🛠️ Technologies Used

### Frontend

- React
- Vite
- JavaScript
- CSS

### Backend

- Python
- FastAPI
- SQLAlchemy

### Machine Learning

- Scikit-learn
- NumPy
- Pandas

### Database

- PostgreSQL

---

# 🌟 Example Workflow

1️⃣ User selects travel preferences
2️⃣ AI recommends destinations
3️⃣ System predicts travel cost
4️⃣ Route planner optimizes path
5️⃣ AI generates travel itinerary
6️⃣ Weather information helps finalize the trip

---

# 🚀 Future Enhancements

- Hotel and transport booking integration
- Mobile application version
- Advanced recommendation algorithms
- Real-time traffic integration

---

# ⭐ Support

If you found this project helpful, consider giving it a **star ⭐ on GitHub**.

---

# 📜 License

This project is developed for **educational and research purposes**.
