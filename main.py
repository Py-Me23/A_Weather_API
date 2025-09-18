# API: OpenWeatherMap
# MongoDB: Save { city, temperature, description, date, user_note }
# Endpoints:
# GET /weather/{city} → fetch live weather + save in DB
# POST /journal → add a note with today’s weather
# GET /journal → list saved weather notes
# 💡 Extra Challenge: Show weather trends (avg temp per city).
# city, temperature, description, date, user_note

from fastapi import FastAPI, HTTPException, status
from db import weather_trends, user_collection
from pydantic import BaseModel, Field, EmailStr
from utils import replace_mongo_id
import os
from dotenv import load_dotenv
from datetime import date


class WeatherTrends(BaseModel):
    city: str
    temperature: str
    description: str
    user_note: str
    date: date


load_dotenv()

app = FastAPI()


@app.get("/", tags=["🌤️🌧️❄️"])
def welcome_user():
    return {"message": "Welcome to our weather info platform"}
