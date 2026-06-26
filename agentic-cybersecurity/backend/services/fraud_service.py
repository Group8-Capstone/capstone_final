import pandas as pd
import joblib

from datetime import datetime


class FraudDetectionService:

    def __init__(self):

        self.model = joblib.load(
            "models/fraud_detection/fraud_model.pkl"
        )

    def predict(self, file_path):

        ##################################################
        # Load Data
        ##################################################

        df = pd.read_csv(file_path)

        ##################################################
        # Prediction
        ##################################################

        predictions = self.model.predict(df)

        probabilities = self.model.predict_proba(df)

        ##################################################
        # Highest Fraud Probability
        ##################################################

        confidence = float(
            probabilities[:, 1].max()
        )

        ##################################################
        # Fraud Count
        ##################################################

        fraud_count = int(predictions.sum())

        ##################################################
        # Final Prediction
        ##################################################

        prediction = (
            "Fraud"
            if fraud_count > 0
            else "Normal"
        )

        ##################################################
        # Risk Level
        ##################################################

        if confidence >= 0.90:

            risk = "HIGH"

        elif confidence >= 0.60:

            risk = "MEDIUM"

        else:

            risk = "LOW"

        ##################################################
        # Response
        ##################################################

        return {

            "prediction": prediction,

            "confidence": round(confidence, 4),

            "risk": risk,

            "model": "XGBoost Fraud Detection",

            "dataset": "Credit Card Fraud",

            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "fraud_detected": fraud_count,

            "total_transactions": len(df),

            "normal_transactions":
                len(df) - fraud_count,

            "predictions":
                predictions.tolist(),

            "probabilities":
                probabilities.tolist()

        }