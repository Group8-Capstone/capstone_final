import datetime


class InvestigationAgent:

    def __init__(self):

        self.investigations = []

        print("=" * 60)
        print("INVESTIGATION AGENT INITIALIZED")
        print("=" * 60)

    def investigate(

        self,

        detection_result,

        ml_result=None,

        rule_result=None,

        ueba_result=None
    ):

        print("=" * 60)
        print("RUNNING THREAT INVESTIGATION")
        print("=" * 60)

        try:

            # =====================================
            # DEFAULT VALUES
            # =====================================

            attack_type = detection_result.get(

                "attack_type",

                "Unknown"
            )

            detection_score = detection_result.get(

                "score",

                0
            )

            detection_status = detection_result.get(

                "status",

                "unknown"
            )

            # =====================================
            # THREAT LEVEL LOGIC
            # =====================================

            if detection_score >= 0.9:

                threat_level = "CRITICAL"

            elif detection_score >= 0.75:

                threat_level = "HIGH"

            elif detection_score >= 0.6:

                threat_level = "MEDIUM"

            else:

                threat_level = "LOW"

            # =====================================
            # THREAT DESCRIPTION
            # =====================================

            threat_descriptions = {

                "DDoS":
                "Distributed denial-of-service "
                "activity detected",

                "Bot":
                "Botnet traffic behavior identified",

                "PortScan":
                "Suspicious port scanning activity "
                "detected",

                "BruteForce":
                "Multiple failed authentication "
                "attempts observed",

                "SQLInjection":
                "Potential SQL injection pattern "
                "detected",

                "Normal":
                "No malicious behavior detected"
            }

            details = threat_descriptions.get(

                attack_type,

                "Suspicious activity identified"
            )

            # =====================================
            # INVESTIGATION RESULT
            # =====================================

            investigation_result = {

                "timestamp": str(
                    datetime.datetime.now()
                ),

                "status": detection_status,

                "attack_type": attack_type,

                "threat_level": threat_level,

                "confidence_score": detection_score,

                "details": details,

                "ml_result": ml_result,

                "rule_result": rule_result,

                "ueba_result": ueba_result
            }

            # =====================================
            # STORE INVESTIGATION
            # =====================================

            self.investigations.append(
                investigation_result
            )

            print(
                f"Threat Level: "
                f"{threat_level}"
            )

            print(
                f"Attack Type: "
                f"{attack_type}"
            )

            print(
                f"Confidence Score: "
                f"{detection_score}"
            )

            print(
                f"Details: "
                f"{details}"
            )

            print("=" * 60)

            return investigation_result

        except Exception as e:

            print(
                f"Investigation error: {e}"
            )

            return {

                "status": "failed",

                "message": str(e)
            }