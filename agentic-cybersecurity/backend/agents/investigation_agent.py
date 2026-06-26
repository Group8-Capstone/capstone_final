import os
import json
import datetime


class InvestigationAgent:

    def __init__(self):

        self.investigations = []

        self.output_dir = (
            "outputs/reports/investigation"
        )

        os.makedirs(
            self.output_dir,
            exist_ok=True
        )

        print("=" * 60)
        print("INVESTIGATION AGENT INITIALIZED")
        print("=" * 60)

    # =====================================================
    # MAIN INVESTIGATION
    # =====================================================

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

            attack_type = detection_result.get(
                "attack_type",
                "Unknown"
            )

            confidence = float(
                detection_result.get(
                    "score",
                    0
                )
            )

            status = detection_result.get(
                "status",
                "unknown"
            )

            severity = detection_result.get(
                "severity",
                "LOW"
            )

            #################################################

            threat_level = self.get_threat_level(
                confidence
            )

            #################################################

            root_cause = self.get_root_cause(
                attack_type
            )

            #################################################

            recommendation = self.get_recommendation(
                attack_type
            )

            #################################################

            mitre = self.get_mitre(
                attack_type
            )

            #################################################

            ioc = self.get_ioc(
                attack_type
            )

            #################################################

            affected_assets = self.get_assets(
                attack_type
            )

            #################################################

            report = {

                "timestamp":

                str(
                    datetime.datetime.now()
                ),

                "status": status,

                "attack_type": attack_type,

                "severity": severity,

                "threat_level": threat_level,

                "confidence": round(
                    confidence,
                    4
                ),

                "root_cause": root_cause,

                "recommendation": recommendation,

                "mitre_mapping": mitre,

                "indicator_of_compromise": ioc,

                "affected_assets": affected_assets,

                "ml_result": ml_result,

                "rule_result": rule_result,

                "ueba_result": ueba_result

            }

            #################################################

            self.investigations.append(
                report
            )

            #################################################

            with open(

                os.path.join(

                    self.output_dir,

                    "investigation_report.json"

                ),

                "w"

            ) as f:

                json.dump(

                    report,

                    f,

                    indent=4

                )

            #################################################

            print(f"Attack Type   : {attack_type}")
            print(f"Threat Level  : {threat_level}")
            print(f"Confidence    : {confidence}")
            print(f"MITRE         : {mitre}")

            print("=" * 60)

            return report

        except Exception as e:

            print(e)

            return {

                "status": "failed",

                "message": str(e)

            }

    # =====================================================
    # THREAT LEVEL
    # =====================================================

    def get_threat_level(self, score):

        if score >= 0.95:

            return "CRITICAL"

        elif score >= 0.85:

            return "HIGH"

        elif score >= 0.70:

            return "MEDIUM"

        return "LOW"

    # =====================================================
    # ROOT CAUSE
    # =====================================================

    def get_root_cause(self, attack):

        mapping = {

            "DDoS":
            "Large volume of malicious network traffic.",

            "PortScan":
            "Reconnaissance activity targeting open ports.",

            "Bot":
            "Compromised endpoint communicating with botnet.",

            "SQLInjection":
            "Malicious SQL query attempting database access.",

            "BruteForce":
            "Repeated authentication failures detected.",

            "Normal":
            "No malicious behaviour detected."

        }

        return mapping.get(

            attack,

            "Unknown activity"

        )

    # =====================================================
    # MITRE
    # =====================================================

    def get_mitre(self, attack):

        mapping = {

            "DDoS": "T1498",

            "PortScan": "T1046",

            "Bot": "T1071",

            "SQLInjection": "T1190",

            "BruteForce": "T1110",

            "Normal": "-"

        }

        return mapping.get(

            attack,

            "-"

        )

    # =====================================================
    # IOC
    # =====================================================

    def get_ioc(self, attack):

        mapping = {

            "DDoS":
            "Abnormal packet rate",

            "PortScan":
            "Multiple sequential port probes",

            "Bot":
            "Beaconing traffic",

            "SQLInjection":
            "Suspicious SQL payload",

            "BruteForce":
            "Repeated login failures",

            "Normal":
            "None"

        }

        return mapping.get(

            attack,

            "Unknown"

        )

    # =====================================================
    # RECOMMENDATION
    # =====================================================

    def get_recommendation(self, attack):

        mapping = {

            "DDoS":
            "Enable rate limiting and block attacker IP.",

            "PortScan":
            "Block source IP and monitor firewall logs.",

            "Bot":
            "Isolate infected endpoint immediately.",

            "SQLInjection":
            "Validate user input and enable WAF.",

            "BruteForce":
            "Lock account and enforce MFA.",

            "Normal":
            "No action required."

        }

        return mapping.get(

            attack,

            "Perform manual investigation."

        )

    # =====================================================
    # AFFECTED ASSETS
    # =====================================================

    def get_assets(self, attack):

        mapping = {

            "DDoS":
            ["Firewall", "Web Server"],

            "PortScan":
            ["Network Gateway"],

            "Bot":
            ["User Endpoint"],

            "SQLInjection":
            ["Application Server", "Database"],

            "BruteForce":
            ["Authentication Server"],

            "Normal":
            []

        }

        return mapping.get(

            attack,

            []
        )

    # =====================================================
    # HISTORY
    # =====================================================

    def get_history(self):

        return self.investigations