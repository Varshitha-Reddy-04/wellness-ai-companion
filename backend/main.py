from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import logs, auth
from models.database import engine
from models.schema import Base

# Ensure DB tables exist
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Wellness AI Companion API",
    description="Backend API with user authentication and personalized weekly tracking.",
    version="2.0.0"
)

# CORS setup for localhost vs deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount routes
app.include_router(auth.router)
app.include_router(logs.router)

@app.get("/")
def home():
    return {"message": "Wellness AI is running 🚀. Please access /docs for the API Swagger UI."}