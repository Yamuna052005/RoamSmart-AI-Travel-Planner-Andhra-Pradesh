import React, { useState } from "react";
import { askAssistant } from "../services/api";

export default function VoiceAssistant() {
  const [query, setQuery] = useState("");
  const [reply, setReply] = useState("");
  const [loading, setLoading] = useState(false);

  // 🔊 Convert reply to speech
  const speakReply = (text) => {
    if (!text) return;
    const utterance = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(utterance);
  };

  const handleSubmit = async () => {
    if (!query.trim()) return;
    setLoading(true);
    setReply("");
    try {
      const res = await askAssistant(query);
      const responseText = res.data.reply || "No reply received";
      setReply(responseText);
      speakReply(responseText); // ✅ Speak the reply
    } catch {
      const errorText = "Failed to fetch assistant reply";
      setReply(errorText);
      speakReply(errorText); // ✅ Speak error too
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="section-bg voice">
      <h2>AI Voice Assistant</h2>
      <input
        placeholder="Ask something..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Thinking..." : "Ask"}
      </button>

      {reply && (
        <div style={{ marginTop: "1rem" }}>
          <strong>Assistant Reply:</strong>
          <p>{reply}</p>
        </div>
      )}
    </div>
  );
}