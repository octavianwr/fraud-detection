# Fraud Detection API

A simple Flask-based machine learning API to detect fraudulent credit card transactions.
Built for Dockerized deployment and end-to-end reproducibility.

## Run Locally
```bash
# 1. Train your model in Jupyter and save it as:
#    app/model/fraud_model.pkl

# 2. Run locally
pip install -r requirements.txt
python app/app.py

# 3. Test API
curl -X GET http://127.0.0.1:5000/status
```

## Run with Docker

```bash
docker build -t fraud-api .
docker run -p 5000:5000 fraud-api
```

## Run Tests

```bash
pytest tests/
```

## Example Request

```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"V1": -1.23, "V2": 0.45, "V3": 0.12, ..., "Amount": 120.0}'
```

Response:

```json
{
  "prediction": 1,
  "fraud_probability": 0.92
}
```
