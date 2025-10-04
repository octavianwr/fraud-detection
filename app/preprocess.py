import numpy as np
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "fraud_model.pkl")

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model file not found. Train and save the model first.")
    return joblib.load(MODEL_PATH)

def preprocess_input(data):
    """
    Expects JSON with numeric features: ['V1', 'V2', ..., 'V28', 'Amount']
    Example:
    {
        "V1": -1.23,
        "V2": 0.45,
        ...
        "Amount": 120.0
    }
    """
    # Sort keys to ensure correct feature order
    ordered_features = [f"V{i}" for i in range(1, 29)] + ["Amount"]
    input_values = [data[feat] for feat in ordered_features]
    return np.array([input_values])
