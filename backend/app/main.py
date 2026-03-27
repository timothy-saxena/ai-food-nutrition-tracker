from fastapi import FastAPI

from .db.database import engine
from .models import meal

meal.Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="AI Food Nutrition Tracker",
    description="Detect food from images and track daily nutrition",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "AI Food Nutrition Tracker API is running"}

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "backend",
        "version": "0.1.0"
    }
