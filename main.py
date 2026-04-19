from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, SensorData
from datetime import datetime

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/add-reading/")
def add_reading(temp: float, hum: float, db: Session = Depends(get_db)):
    reading = SensorData(
        temperature=temp,
        humidity=hum,
        timestamp=datetime.utcnow()
    )
    db.add(reading)
    db.commit()
    db.refresh(reading)
    return reading

@app.get("/readings/")
def get_readings(db: Session = Depends(get_db)):
    return db.query(SensorData).all()

@app.get("/average-temperature/")
def average_temperature(db: Session = Depends(get_db)):
    data = db.query(SensorData).all()
    avg = sum(r.temperature for r in data) / len(data) if data else 0
    return {"average_temperature": avg}

@app.get("/min-max-temperature/")
def min_max_temperature(db: Session = Depends(get_db)):
    data = db.query(SensorData).all()
    if not data:
        return {"min": 0, "max": 0}

    temps = [r.temperature for r in data]

    return {
        "min": min(temps),
        "max": max(temps)
    }