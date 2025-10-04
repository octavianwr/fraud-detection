from flask import Flask, request, jsonify
from preprocess import load_model, preprocess_input
import traceback

app = Flask(__name__)

# Load model once at startup
model = load_model()

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "Fraud Detection API running"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Empty request"}), 400
        
        # Preprocess input
        features = preprocess_input(data)
        prediction = model.predict(features)[0]
        proba = model.predict_proba(features)[0][1]

        return jsonify({
            "prediction": int(prediction),
            "fraud_probability": float(proba)
        }), 200

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
