from pathlib import Path
from typing import Literal

import joblib
import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


ROOT = Path(__file__).resolve().parent.parent
MODEL = joblib.load(ROOT / "telco_churn_model.pkl")
SCALER = joblib.load(ROOT / "telco_scaler.pkl")
FEATURE_COLUMNS = joblib.load(ROOT / "feature_columns.pkl")


class CustomerInput(BaseModel):
    gender: Literal["Male", "Female"]
    senior_citizen: Literal[0, 1]
    partner: Literal["Yes", "No"]
    dependents: Literal["Yes", "No"]
    tenure: int = Field(ge=0, le=100)
    phone_service: Literal["Yes", "No"]
    multiple_lines: Literal["Yes", "No", "No phone service"]
    internet_service: Literal["DSL", "Fiber optic", "No"]
    online_security: Literal["Yes", "No", "No internet service"]
    online_backup: Literal["Yes", "No", "No internet service"]
    device_protection: Literal["Yes", "No", "No internet service"]
    tech_support: Literal["Yes", "No", "No internet service"]
    streaming_tv: Literal["Yes", "No", "No internet service"]
    streaming_movies: Literal["Yes", "No", "No internet service"]
    contract: Literal["Month-to-month", "One year", "Two year"]
    paperless_billing: Literal["Yes", "No"]
    payment_method: Literal[
        "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
    ]
    monthly_charges: float = Field(ge=0, le=1000)
    total_charges: float = Field(ge=0, le=1000000)


class PredictionResponse(BaseModel):
    prediction: Literal["Yes", "No"]
    probability: float
    risk_level: Literal["Low", "Medium", "High"]
    message: str
    contributions: list[dict[str, float | str]]
    recommendations: list[str]


app = FastAPI(title="Telco Customer Churn AI", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins - same-origin on Vercel, localhost in dev
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


def build_features(customer: CustomerInput) -> np.ndarray:
    tenure = customer.tenure
    avg_monthly_spend = customer.total_charges / tenure if tenure else customer.monthly_charges
    values = {
        "SeniorCitizen": customer.senior_citizen, "tenure": tenure,
        "MonthlyCharges": customer.monthly_charges, "TotalCharges": customer.total_charges,
        "AvgMonthlySpend": avg_monthly_spend, "IsNewCustomer": int(tenure < 6),
        "gender_Male": int(customer.gender == "Male"), "Partner_Yes": int(customer.partner == "Yes"),
        "Dependents_Yes": int(customer.dependents == "Yes"), "PhoneService_Yes": int(customer.phone_service == "Yes"),
        "MultipleLines_No phone service": int(customer.multiple_lines == "No phone service"),
        "MultipleLines_Yes": int(customer.multiple_lines == "Yes"),
        "InternetService_Fiber optic": int(customer.internet_service == "Fiber optic"),
        "InternetService_No": int(customer.internet_service == "No"),
        "OnlineSecurity_No internet service": int(customer.online_security == "No internet service"),
        "OnlineSecurity_Yes": int(customer.online_security == "Yes"),
        "OnlineBackup_No internet service": int(customer.online_backup == "No internet service"),
        "OnlineBackup_Yes": int(customer.online_backup == "Yes"),
        "DeviceProtection_No internet service": int(customer.device_protection == "No internet service"),
        "DeviceProtection_Yes": int(customer.device_protection == "Yes"),
        "TechSupport_No internet service": int(customer.tech_support == "No internet service"),
        "TechSupport_Yes": int(customer.tech_support == "Yes"),
        "StreamingTV_No internet service": int(customer.streaming_tv == "No internet service"),
        "StreamingTV_Yes": int(customer.streaming_tv == "Yes"),
        "StreamingMovies_No internet service": int(customer.streaming_movies == "No internet service"),
        "StreamingMovies_Yes": int(customer.streaming_movies == "Yes"),
        "Contract_One year": int(customer.contract == "One year"), "Contract_Two year": int(customer.contract == "Two year"),
        "PaperlessBilling_Yes": int(customer.paperless_billing == "Yes"),
        "PaymentMethod_Credit card (automatic)": int(customer.payment_method == "Credit card (automatic)"),
        "PaymentMethod_Electronic check": int(customer.payment_method == "Electronic check"),
        "PaymentMethod_Mailed check": int(customer.payment_method == "Mailed check"),
    }
    return np.asarray([[values[column] for column in FEATURE_COLUMNS]], dtype=float)


def risk_for(probability: float) -> str:
    return "High" if probability >= 0.7 else "Medium" if probability >= 0.4 else "Low"


def explain(customer: CustomerInput, raw_features: np.ndarray) -> tuple[list[dict[str, float | str]], list[str]]:
    scaled = SCALER.transform(raw_features)[0]
    contributions = [{"feature": column, "impact": round(float(value), 4)} for column, value in sorted(
        zip(FEATURE_COLUMNS, scaled * MODEL.coef_[0]), key=lambda item: abs(item[1]), reverse=True
    )[:6]]
    recommendations = []
    if customer.contract == "Month-to-month":
        recommendations.append("Consider a longer-term contract offer for this month-to-month customer.")
    if customer.payment_method == "Electronic check":
        recommendations.append("Review electronic-check customers for billing friction or payment incentives.")
    if customer.tenure < 6:
        recommendations.append("Prioritize early-lifecycle outreach and onboarding support.")
    if not recommendations:
        recommendations.append("Continue proactive service check-ins and monitor this account over time.")
    return contributions, recommendations


@app.get("/health")
def health() -> dict[str, str | int]:
    return {"status": "ok", "model": type(MODEL).__name__, "features": len(FEATURE_COLUMNS)}


@app.post("/predict", response_model=PredictionResponse)
def predict(customer: CustomerInput) -> PredictionResponse:
    features = build_features(customer)
    scaled = SCALER.transform(features)
    probability = float(MODEL.predict_proba(scaled)[0, 1])
    prediction = "Yes" if int(MODEL.predict(scaled)[0]) == 1 else "No"
    risk_level = risk_for(probability)
    contributions, recommendations = explain(customer, features)
    status = "high predicted churn risk" if prediction == "Yes" else "likely to stay"
    return PredictionResponse(prediction=prediction, probability=probability, risk_level=risk_level,
                              message=f"This customer has {status}.", contributions=contributions,
                              recommendations=recommendations)