import pandas as pd
import joblib


class FraudDetectionService:

    def __init__(self):

        self.model = joblib.load(
            'models/fraud_detection/fraud_model.pkl'
        )

    def predict(self, file_path):

        df = pd.read_csv(file_path)

        predictions = self.model.predict(df)

        probabilities = self.model.predict_proba(df)

        return {
            "predictions": predictions.tolist(),
            "probabilities": probabilities.tolist(),
            "fraud_detected": int(sum(predictions))
        }