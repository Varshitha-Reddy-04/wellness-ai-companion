# 🧠 AI Mental Wellness Companion

An intelligent, AI-powered mental wellness tracker designed for students. It combines **real-time facial emotion detection**, **NLP sentiment analysis**, **rule-based pattern detection**, and **predictive weekly forecasting** to help users monitor and improve their mental health.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.135-green?logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 **User Authentication** | JWT-based signup/login with bcrypt password hashing |
| 📊 **Personalized Dashboard** | Glassmorphism-themed UI with Chart.js mood trend visualization |
| 📝 **Smart Journaling** | NLP-powered sentiment analysis of journal entries using TextBlob |
| 🎯 **Burnout Score** | Real-time burnout risk calculation (0-100) based on mood, sleep, work hours |
| 🔍 **Pattern Detection** | Rule-based engine detects low mood streaks, overwork patterns, and screen-sleep correlation |
| 📅 **Weekly AI Forecast** | Predictive engine analyzes 7-day trends and generates personalized schedule adjustments |
| 📷 **AI Camera Mode** | Real-time facial emotion detection via face-api.js with auto-logging |
| 🎵 **Emotional Support** | Motivational quotes and music recommendations based on mood |

---

## 🏗️ Architecture

```
wellnessproject/
├── backend/
│   ├── main.py                  # FastAPI app entry point
│   ├── models/
│   │   ├── database.py          # SQLAlchemy engine & session
│   │   └── schema.py            # DB models (User, Log) & Pydantic schemas
│   ├── routers/
│   │   ├── auth.py              # /auth/signup, /auth/login endpoints
│   │   └── logs.py              # /log, /history, /insights/weekly endpoints
│   ├── logic/
│   │   ├── auth_handler.py      # JWT token creation & validation, bcrypt hashing
│   │   ├── helpers.py           # Burnout calculation, suggestions, quotes
│   │   ├── ai_analyzer.py       # NLP sentiment analysis (TextBlob)
│   │   ├── rule_engine.py       # Pattern detection (streaks, correlations)
│   │   └── weekly_analyzer.py   # Predictive weekly forecast engine
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   └── index.html               # Single-page glassmorphism UI
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip

### Backend Setup

```bash
cd backend
python -m venv venv

# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt_tab')"
uvicorn main:app --reload
```

Backend runs at `http://localhost:8000`. API docs at `http://localhost:8000/docs`.

### Frontend Setup

```bash
cd frontend
python -m http.server 5500
```

Open `http://localhost:5500` in your browser.

---

## 🔑 API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| `POST` | `/auth/signup` | ❌ | Create a new account |
| `POST` | `/auth/login` | ❌ | Login and receive JWT token |
| `POST` | `/log` | ✅ | Submit a daily wellness log |
| `GET` | `/history` | ✅ | Get all logs for the authenticated user |
| `GET` | `/insights/weekly` | ✅ | Get AI-generated weekly forecast & suggestions |

---

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3 (Glassmorphism), JavaScript, Chart.js, face-api.js
- **Backend:** Python, FastAPI, SQLAlchemy, SQLite
- **AI/ML:** TextBlob (NLP), face-api.js (Emotion Detection), Rule-based Pattern Engine
- **Auth:** JWT (PyJWT), bcrypt
- **Deployment:** Docker-ready

---

## 📄 License

This project is licensed under the MIT License.
