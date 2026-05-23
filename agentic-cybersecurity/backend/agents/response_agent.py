import datetime


class ResponseAgent:

    def __init__(self):

        self.responses = []

        print("=" * 60)
        print("RESPONSE AGENT INITIALIZED")
        print("=" * 60)

    def respond(self, investigation_result):

        print("=" * 60)
        print("GENERATING INCIDENT RESPONSE")
        print("=" * 60)

        try:

            # =====================================
            # EXTRACT DATA
            # =====================================

            threat_level = investigation_result.get(

                "threat_level",

                "LOW"
            )

            attack_type = investigation_result.get(

                "attack_type",

                "Unknown"
            )

            confidence_score = investigation_result.get(

                "confidence_score",

                0
            )

            # =====================================
            # RESPONSE ACTION LOGIC
            # =====================================

            if threat_level == "CRITICAL":

                action = "BLOCK_IP"

                status = "executed"

                mitigation = (

                    "Source IP blocked immediately"
                )

            elif threat_level == "HIGH":

                action = "ISOLATE_SYSTEM"

                status = "executed"

                mitigation = (

                    "Affected endpoint isolated "
                    "from network"
                )

            elif threat_level == "MEDIUM":

                action = "ALERT_ADMIN"

                status = "pending"

                mitigation = (

                    "Security administrator "
                    "notification triggered"
                )

            else:

                action = "MONITOR"

                status = "monitoring"

                mitigation = (

                    "Continuous monitoring enabled"
                )

            # =====================================
            # RESPONSE RESULT
            # =====================================

            response_result = {

                "timestamp": str(
                    datetime.datetime.now()
                ),

                "attack_type": attack_type,

                "threat_level": threat_level,

                "confidence_score": confidence_score,

                "action": action,

                "status": status,

                "mitigation": mitigation
            }

            # =====================================
            # STORE RESPONSE
            # =====================================

            self.responses.append(
                response_result
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
                f"Response Action: "
                f"{action}"
            )

            print(
                f"Response Status: "
                f"{status}"
            )

            print(
                f"Mitigation: "
                f"{mitigation}"
            )

            print("=" * 60)

            return response_result

        except Exception as e:

            print(
                f"Response generation error: {e}"
            )

            return {

                "status": "failed",

                "message": str(e)
            }