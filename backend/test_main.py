from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)
VALID_CUSTOMER = {
    "gender": "Female", "senior_citizen": 0, "partner": "No", "dependents": "No", "tenure": 2,
    "phone_service": "Yes", "multiple_lines": "No", "internet_service": "Fiber optic",
    "online_security": "No", "online_backup": "No", "device_protection": "No", "tech_support": "No",
    "streaming_tv": "Yes", "streaming_movies": "Yes", "contract": "Month-to-month",
    "paperless_billing": "Yes", "payment_method": "Electronic check", "monthly_charges": 85.5,
    "total_charges": 171.0,
}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["features"] == 32

def test_prediction_returns_real_probability():
    response = client.post("/predict", json=VALID_CUSTOMER)
    body = response.json()
    assert response.status_code == 200
    assert body["prediction"] in {"Yes", "No"}
    assert 0 <= body["probability"] <= 1
    assert body["contributions"]

def test_invalid_negative_charges_are_rejected():
    assert client.post("/predict", json={**VALID_CUSTOMER, "monthly_charges": -1}).status_code == 422