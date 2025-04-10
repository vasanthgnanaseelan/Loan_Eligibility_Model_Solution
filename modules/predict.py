# modules/predict.py

import pickle
import logging
import pandas as pd

def load_model(model_path: str = "models/loan_model.pkl"):
    try:
        with open(model_path, 'rb') as f:
            model, label_encoders, target_encoder = pickle.load(f)
        logging.info("Model loaded successfully from %s", model_path)
        return model, label_encoders, target_encoder
    except Exception as e:
        logging.error("Error loading model: %s", e)
        raise

def predict_loan_approval(user_input: dict, model, label_encoders, target_encoder) -> str:
    try:
        df_input = pd.DataFrame([user_input])
        for col, le in label_encoders.items():
            df_input[col] = le.transform(df_input[col])
        prediction = model.predict(df_input)[0]
        result = target_encoder.inverse_transform([prediction])[0]
        return result
    except Exception as e:
        logging.error("Prediction error: %s", e)
        raise
