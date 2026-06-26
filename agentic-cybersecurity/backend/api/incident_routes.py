import os
import json

from fastapi import APIRouter

router = APIRouter(
    tags=["Incident Response"]
)

REPORT_DIR = "outputs/reports/response"


# =====================================================
# INCIDENT RESPONSE
# =====================================================

@router.get("/api/incident-response")
def incident_response():

    report_file = os.path.join(
        REPORT_DIR,
        "response_report.json"
    )

    if not os.path.exists(report_file):

        return [

            {

                "title": "No Incident",

                "description":
                "No response report available.",

                "status": "Waiting"

            }

        ]

    try:

        with open(report_file, "r") as f:

            report = json.load(f)

        return [

            {

                "title": report.get(

                    "response_action",

                    "Unknown"

                ),

                "description":

                f"Attack: {report.get('attack_type','Unknown')} | "

                f"Threat: {report.get('threat_level','LOW')} | "

                f"Firewall: {report.get('firewall_action','-')} | "

                f"Endpoint: {report.get('endpoint_action','-')}",

                "status": report.get(

                    "status",

                    "Completed"

                )

            },

            {

                "title": "SOC Notification",

                "description":

                report.get(

                    "soc_notification",

                    "Not Required"

                ),

                "status": "Sent"

            },

            {

                "title": "Recovery Estimate",

                "description":

                report.get(

                    "estimated_recovery",

                    "Unknown"

                ),

                "status": "Planned"

            },

            {

                "title": "Playbook",

                "description":

                report.get(

                    "playbook",

                    "Generic Playbook"

                ),

                "status": "Executed"

            }

        ]

    except Exception as e:

        return [

            {

                "title": "Error",

                "description": str(e),

                "status": "Failed"

            }

        ]


# =====================================================
# LATEST RESPONSE REPORT
# =====================================================

@router.get("/api/incident-report")
def incident_report():

    report_file = os.path.join(
        REPORT_DIR,
        "response_report.json"
    )

    if not os.path.exists(report_file):

        return {

            "status": "No Report"

        }

    with open(report_file, "r") as f:

        return json.load(f)