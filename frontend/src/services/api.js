import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "https://legalbot-production-881a.up.railway.app",
  timeout: 30000,
  headers: {
    "Content-Type": "application/json",
  },
});

export const askQuestion = async (message) => {
  try {
    const response = await API.post("/api/v1/chat", {
      message,
    });

    return response.data.data;
  } catch (error) {
    console.error("API Error:", error);
    throw error;
  }
};