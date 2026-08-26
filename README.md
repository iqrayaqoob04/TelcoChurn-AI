# Telco Customer Churn AI

A production-style FastAPI and React application connected to the supplied Telco churn artifacts. It does not retrain or replace the model.

## Verified model contract

- `telco_churn_model.pkl`: joblib-serialized `LogisticRegression`, classes `[0, 1]`, 32 inputs, `predict_proba` supported.
- `telco_scaler.pkl`: joblib-serialized `StandardScaler` fitted on the exact 32 columns.
- `feature_columns.pkl`: exact feature order, including `AvgMonthlySpend = TotalCharges / tenure` (with monthly charges used when tenure is zero) and `IsNewCustomer = tenure < 6`.
- One-hot encoding uses the saved column names; baseline categories are represented by all-zero columns.

## Run

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd ..
python -m uvicorn backend.main:app --reload --port 8000
```

In a second terminal:

```powershell
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`. The API is `POST /predict`; `GET /health` reports the loaded model and feature count.

## Example request

Send the fields shown in the frontend form. Numeric values are validated as non-negative. The response includes `prediction`, probability, risk level, coefficient-based model signals, and contextual recommendations. Feature signals are calculated from the actual scaled feature values and trained logistic coefficients; no feature importance is fabricated.

## Deployment

Build the frontend with `npm run build`, serve `frontend/dist`, and run the backend behind a process manager or container. Set `VITE_API_URL` at frontend build time and restrict `allow_origins` in `backend/main.py` to the deployed frontend origin.

### Vercel

Import this GitHub repository into Vercel with the repository root as the project root. The included `vercel.json` builds `frontend` and exposes the FastAPI app at `/api`. Leave `VITE_API_URL` unset for the same-origin default, or set it to `/api`. Vercel will install the root `requirements.txt` for the Python function.