
from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
import joblib

# Create the FastAPI application
app = FastAPI(title="Titanic Survival Prediction API")

# Load the trained model
model = joblib.load("models/model.joblib")


# Define passenger input
class Passenger(BaseModel):
    Pclass: int = Field(ge=1, le=3)
    Sex: str
    Age: float = Field(ge=0, le=100)
    SibSp: int = Field(ge=0)
    Parch: int = Field(ge=0)
    Fare: float = Field(ge=0)
    Embarked: str


@app.get("/")
def home():
    return {
        "message": "Titanic Survival Prediction API is running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(passenger: Passenger):
    data = pd.DataFrame([passenger.model_dump()])

    prediction = int(model.predict(data)[0])

    return {
        "prediction": prediction,
        "survival_status": (
            "Survived" if prediction == 1
            else "Did not survive"
        )
    }
