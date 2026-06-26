import numpy as np

from agents.ml_agent import MLAgent


class DetectionAgent:

    def __init__(self, threshold=0.70):

        self.threshold = threshold

        self.ml_agent = MLAgent()

        self.alerts = []

        print("=" * 60)
        print("DETECTION AGENT INITIALIZED")
        print("=" * 60)

    def detect(self, data):

        print("=" * 60)
        print("RUNNING THREAT DETECTION")
        print("=" * 60)

        try:

            # =====================================
            # VALIDATE INPUT
            # =====================================

            if data is None:

                return {
                    "status": "failed",
                    "message": "Input data is None"
                }

            if not isinstance(data, np.ndarray):

                data = np.array(data)

            if len(data) == 0:

                return {
                    "status": "failed",
                    "message": "Empty input data"
                }

            data = data.astype(np.float32)

            # =====================================
            # RUN ML MODELS
            # =====================================

            prediction = self.ml_agent.predict(data)

            attack_type = prediction.get(
                "prediction",
                "Unknown"
            )

            confidence = float(
                prediction.get(
                    "confidence",
                    0
                )
            )

            # =====================================
            # DETERMINE STATUS
            # =====================================

            if confidence >= self.threshold:

                status = "anomaly_detected"

            else:

                status = "normal"

            # =====================================
            # DETERMINE SEVERITY
            # =====================================

            if confidence >= 0.95:

                severity = "CRITICAL"

            elif confidence >= 0.85:

                severity = "HIGH"

            elif confidence >= 0.70:

                severity = "MEDIUM"

            else:

                severity = "LOW"

            # =====================================
            # BUILD ALERT
            # =====================================

            alert = {

                "status": status,

                "attack_type": attack_type,

                "severity": severity,

                "score": round(
                    confidence,
                    4
                ),

                "cnn_confidence": prediction.get(
                    "cnn_confidence",
                    0
                ),

                "transformer_confidence": prediction.get(
                    "transformer_confidence",
                    0
                ),

                "records_analyzed": int(
                    len(data)
                )
            }

            self.alerts.append(alert)

            print(f"Detection Status : {status}")
            print(f"Attack Type      : {attack_type}")
            print(f"Severity         : {severity}")
            print(f"Confidence       : {confidence:.4f}")
            print(f"Records          : {len(data)}")

            print("=" * 60)

            return alert

        except Exception as e:

            print(f"Detection Error : {e}")

            return {

                "status": "failed",

                "message": str(e)
            }

    # =====================================
    # GET ALERT HISTORY
    # =====================================

    def get_alerts(self):

        return self.alerts

    # =====================================
    # CLEAR ALERT HISTORY
    # =====================================

    def clear_alerts(self):

        self.alerts.clear()

        print("Alert history cleared.")