# 🧠 AI-Powered Data Logging & Retrieval via Chatbot

An AI system that:
- Records **video**, **images**, and **text** logs
- Stores them in a **database and/or GCP Storage**
- Embeds logs for semantic search
- Allows **chatbot-based querying** via **OpenAI or Ollama LLM**
- Supports **face recognition** and **motion detection**
- Deploys to **Render (backend)** and **Vercel (frontend)**

---

## 📦 Features

| Feature                        | Description |
|-------------------------------|-------------|
| 🎥 Video/Image Capture        | Capture from camera in real-time |
| 📝 Text Logging               | Manual input or event-based logs |
| 🧠 LLM Chatbot                | Ask chatbot to retrieve matching logs |
| 📂 GCP Storage Support        | Store media files on Google Cloud |
| 🔎 Semantic Search            | Embedding-based search via FAISS (optional) |
| 🧍 Face Recognition           | Face detection with OpenCV |
| 🎞️ Motion Detection          | Detect activity via frame deltas |
| 🧠 Dual LLM Support           | Use OpenAI API or local Ollama LLM |
| 🌐 Web App                    | Frontend with React, backend with Flask |

---

## 🗂️ Project Structure

```
ai_data_logger_chatbot/
├── backend/
│   ├── app.py                  # Main Flask app
│   ├── camera_module.py        # Video capture + face/motion detection
│   ├── chatbot_module.py       # LLM chatbot engine
│   ├── gcp_module.py           # GCP storage uploader
│   ├── db_module.py            # Database interaction logic
│   └── utils/
│       ├── embedder.py         # Embedding generator
│       ├── openai_chain.py     # OpenAI query logic
│       └── ollama_chain.py     # Ollama (LangChain) interface
├── frontend/
│   ├── src/
│   │   ├── App.jsx             # Main React app
│   │   ├── Chatbot.jsx         # Chat interface
│   │   ├── VideoRecorder.jsx   # Live camera
│   │   └── ImageGallery.jsx    # Log viewer
├── database/schema.sql         # PostgreSQL or MySQL schema
├── ai_models/                  # Embedding/vector store (if local)
├── scripts/embed_all.py        # Index all logs into embedding store
├── docker-compose.yml          # Compose setup
├── README.md                   # This file
```

---

## 🔐 Environment Variables

Create a `.env` file in `backend/` with the following:

```env
OPENAI_API_KEY=your_openai_api_key
GCP_BUCKET_NAME=your_gcp_bucket
GOOGLE_APPLICATION_CREDENTIALS=path_to_gcp_credentials.json
```

---

## 🚀 Deployment Guide

### Backend (Flask) on [Render](https://render.com)
1. Push `/backend/` to GitHub
2. Create new Web Service on Render
3. Set Python build, add environment variables (`.env`)
4. Expose port `5000`

### Frontend (React) on [Vercel](https://vercel.com)
1. Push `/frontend/` to GitHub
2. Import project into Vercel
3. Set backend endpoint in `.env` or config file

---

## 🧪 Run Locally

```bash
# From root
docker-compose up --build
```

Backend will be at: `http://localhost:5000`  
Frontend at: `http://localhost:3000`

---

## 💬 Chatbot Query Example

> **You**: "What did the front camera see yesterday at 3 PM?"  
> **Bot**: "Here's an image with a person near the shelf around that time." *(Includes image & text)*

---

## 🛠 Requirements

- Docker & Docker Compose
- OpenCV
- Google Cloud SDK (for GCP storage)
- Python 3.9+
- React 18+

---

## 📚 Future Improvements
- Add FAISS/ChromaDB vector search
- Support multi-camera inputs
- Integrate LLM fine-tuning
- Streamlit dashboard for monitoring
