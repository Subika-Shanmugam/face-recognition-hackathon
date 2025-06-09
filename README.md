# 👁️‍🗨️ Face Recognition Hackathon Project

This project was built as part of the **Katomaran AI Hackathon**, with the goal of creating a real-time browser-based platform for face recognition and AI-powered Q&A using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

### 🔐 Face Registration
- Accesses webcam via browser (React.js)
- Detects faces using Python (`face_recognition` library)
- Captures and saves face encodings with metadata (name, timestamp)
- Stores in a chosen database (e.g., JSON or MongoDB)

### 🎥 Live Face Recognition
- Streams webcam in real time
- Recognizes registered faces using stored encodings
- Supports multiple face detection in one frame
- Shows bounding boxes with names

### 💬 Chat-Based Q&A (RAG)
- Embedded React chat widget
- Uses WebSocket to connect: React ↔ Node.js ↔ Python
- RAG engine powered by:
  - LangChain
  - FAISS for vector search
  - OpenAI GPT-3.5/4 for generating responses
- Answers queries like:
  - “Who was the last person registered?”
  - “At what time was Karthik registered?”
  - “How many people are currently registered?”

---

## 🧱 Tech Stack

| Module | Technology |
|--------|------------|
| Frontend | React.js |
| Backend | Node.js (API + WebSocket) |
| Face Recognition | Python (`face_recognition`) |
| RAG Engine | Python (LangChain + FAISS + OpenAI) |
| Database | JSON / MongoDB / your choice |
| LLM | OpenAI GPT-3.5 or GPT-4 |

---

## 🏗️ Project Structure

