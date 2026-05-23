import numpy as np


class DetectionAgent:

    def __init__(

        self,

        models=None,

        threshold=0.7
    ):

        self.models = models

        self.threshold = threshold

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

            # =====================================
            # CONVERT TO NUMPY
            # =====================================

            if not isinstance(
                data,
                np.ndarray
            ):

                data = np.array(data)

            # =====================================
            # HANDLE EMPTY INPUT
            # =====================================

            if len(data) == 0:

                return {

                    "status": "failed",

                    "message": "Empty input data"
                }

            # =====================================
            # DUMMY PREDICTION LOGIC
            # =====================================

            anomaly_score = round(

                np.random.uniform(
                    0.5,
                    1.0
                ),

                4
            )

            # =====================================
            # ATTACK LABELS
            # =====================================

            attack_types = [

                'DDoS',

                'Bot',

                'PortScan',

                'BruteForce',

                'SQLInjection',

                'Normal'
            ]

            predicted_attack = np.random.choice(
                attack_types
            )

            # =====================================
            # THREAT STATUS
            # =====================================

            if anomaly_score >= self.threshold:

                status = "anomaly_detected"

                severity = "HIGH"

            else:

                status = "normal"

                severity = "LOW"

            # =====================================
            # CREATE ALERT
            # =====================================

            alert = {

                "status": status,

                "attack_type": predicted_attack,

                "severity": severity,

                "score": float(
                    anomaly_score
                ),

                "records_analyzed": int(
                    len(data)
                )
            }

            # =====================================
            # STORE ALERT
            # =====================================

            self.alerts.append(alert)

            print(
                f"Detection Status: "
                f"{status}"
            )

            print(
                f"Attack Type: "
                f"{predicted_attack}"
            )

            print(
                f"Confidence Score: "
                f"{anomaly_score}"
            )

            print(
                f"Records Analyzed: "
                f"{len(data)}"
            )

            print("=" * 60)

            return alert

        except Exception as e:

            print(
                f"Detection error: {e}"
            )

            return {

                "status": "failed",

                "message": str(e)
            }