import { useState } from "react";
import "./App.css";
import Destinations from "./components/Destinations";
import Recommend from "./components/Recommend";
import CostPredict from "./components/CostPredict";
import Weather from "./components/Weather";
import RoutePlanner from "./components/RoutePlanner";
import VoiceAssistant from "./components/VoiceAssistant";

function App() {
  const [activeTab, setActiveTab] = useState("destinations");

  const renderContent = () => {
    switch (activeTab) {
      case "destinations":
        return <Destinations />;
      case "recommend":
        return <Recommend />;
      case "cost":
        return (
          <div className="section-bg cost">
            <CostPredict />
          </div>
        );
      case "weather":
        return (
          <div className="section-bg weather">
            <Weather />
          </div>
        );
      case "route":
        return (
          <div className="section-bg route">
            <RoutePlanner />
          </div>
        );
      case "assistant":
        return (
          <div className="section-bg voice">
            <VoiceAssistant />
          </div>
        );
      default:
        return <Destinations />;
    }
  };

  return (
    <div className="dashboard">
      {/* Sidebar Navigation */}
      <nav>
        <h2>RoamSmart AI Travel Planner For Andhra Pradesh</h2>
        <ul>
          <li onClick={() => setActiveTab("destinations")}>🌍 Destinations</li>
          <li onClick={() => setActiveTab("recommend")}>🤖 Recommendations</li>
          <li onClick={() => setActiveTab("cost")}>💰 Cost Predictor</li>
          <li onClick={() => setActiveTab("weather")}>☁️ Weather</li>
          <li onClick={() => setActiveTab("route")}>🗺️ Route Planner</li>
          <li onClick={() => setActiveTab("assistant")}>🎙️ Voice Assistant</li>
        </ul>
      </nav>

      {/* Main Content */}
      <main>{renderContent()}</main>
    </div>
  );
}

export default App;