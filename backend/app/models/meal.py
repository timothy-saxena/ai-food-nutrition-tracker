from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db.database import Base

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    meal_name = Column(String, nullable=False)
    calories = Column(Float)
    carbs = Column(Float)
    protein = Column(Float)
    fat = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)