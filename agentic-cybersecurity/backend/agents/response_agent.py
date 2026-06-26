import os
import json
import datetime


class ResponseAgent:

    def __init__(self):

        self.responses = []

        self.output_dir = (
            "outputs/reports/response"
        )

        os.makedirs(
            self.output_dir,
            exist_ok=True
        )

        print("=" * 60)
        print("RESPONSE AGENT INITIALIZED")
        print("=" * 60)

    # =====================================================
    # INCIDENT RESPONSE
    # =====================================================

    def respond(self, investigation_result):

        print("=" * 60)
        print("GENERATING INCIDENT RESPONSE")
        print("=" * 60)

        try:

            attack_type = investigation_result.get(
                "attack_type",
                "Unknown"
            )

            threat_level = investigation_result.get(
                "threat_level",
                "LOW"
            )

            confidence = investigation_result.get(
                "confidence",
                0
            )

            #################################################

            action = self.get_action(
                threat_level
            )

            firewall = self.get_firewall_action(
                attack_type
            )

            endpoint = self.get_endpoint_action(
                threat_level
            )

            notification = self.get_soc_notification(
                threat_level
            )

            recovery = self.get_recovery_time(
                threat_level
            )

            playbook = self.get_playbook(
                attack_type
            )

            #################################################

            report = {

                "timestamp":
                str(
                    datetime.datetime.now()
                ),

                "attack_type":
                attack_type,

                "threat_level":
                threat_level,

                "confidence":
                round(
                    float(confidence),
                    4
                ),

                "response_action":
                action,

                "firewall_action":
                firewall,

                "endpoint_action":
                endpoint,

                "soc_notification":
                notification,

                "estimated_recovery":
                recovery,

                "playbook":
                playbook,

                "status":
                "Completed"

            }

            #################################################

            self.responses.append(
                report
            )

            #################################################

            with open(

                os.path.join(

                    self.output_dir,

                    "response_report.json"

                ),

                "w"

            ) as f:

                json.dump(

                    report,

                    f,

                    indent=4

                )

            #################################################

            print(f"Attack Type      : {attack_type}")
            print(f"Threat Level     : {threat_level}")
            print(f"Action           : {action}")
            print(f"Firewall         : {firewall}")
            print(f"Endpoint         : {endpoint}")
            print(f"SOC Notification : {notification}")

            print("=" * 60)

            return report

        except Exception as e:

            print(e)

            return {

                "status": "failed",

                "message": str(e)

            }

    # =====================================================
    # RESPONSE ACTION
    # =====================================================

    def get_action(self, level):

        mapping = {

            "CRITICAL":
            "Block Traffic Immediately",

            "HIGH":
            "Isolate Endpoint",

            "MEDIUM":
            "Notify Security Team",

            "LOW":
            "Continue Monitoring"

        }

        return mapping.get(

            level,

            "Manual Investigation"

        )

    # =====================================================
    # FIREWALL
    # =====================================================

    def get_firewall_action(self, attack):

        mapping = {

            "DDoS":
            "Block Source IP",

            "PortScan":
            "Close Target Ports",

            "Bot":
            "Block Command & Control",

            "SQLInjection":
            "Enable WAF Rule",

            "BruteForce":
            "Rate Limit Login Requests",

            "Normal":
            "No Action"

        }

        return mapping.get(

            attack,

            "Review Firewall"

        )

    # =====================================================
    # ENDPOINT
    # =====================================================

    def get_endpoint_action(self, level):

        if level == "CRITICAL":

            return "Disconnect Endpoint"

        elif level == "HIGH":

            return "Isolate Endpoint"

        elif level == "MEDIUM":

            return "Scan Endpoint"

        return "No Action"

    # =====================================================
    # SOC
    # =====================================================

    def get_soc_notification(self, level):

        if level in [

            "CRITICAL",

            "HIGH"

        ]:

            return "Immediate"

        elif level == "MEDIUM":

            return "Within 30 Minutes"

        return "Not Required"

    # =====================================================
    # RECOVERY
    # =====================================================

    def get_recovery_time(self, level):

        mapping = {

            "CRITICAL":
            "4-6 Hours",

            "HIGH":
            "2-4 Hours",

            "MEDIUM":
            "30-60 Minutes",

            "LOW":
            "Monitoring Only"

        }

        return mapping.get(

            level,

            "Unknown"

        )

    # =====================================================
    # PLAYBOOK
    # =====================================================

    def get_playbook(self, attack):

        mapping = {

            "DDoS":
            "DDoS Mitigation Playbook",

            "PortScan":
            "Reconnaissance Playbook",

            "Bot":
            "Botnet Containment Playbook",

            "SQLInjection":
            "Web Application Playbook",

            "BruteForce":
            "Credential Attack Playbook",

            "Normal":
            "No Response Required"

        }

        return mapping.get(

            attack,

            "Generic Incident Response"

        )

    # =====================================================
    # HISTORY
    # =====================================================

    def get_history(self):

        return self.responses