from fastapi import APIRouter

from services.orchestrator_service import (
    orchestrator
)

router = APIRouter(
    tags=["Investigation"]
)

# =====================================
# GET ALL INVESTIGATIONS
# =====================================

@router.get("/api/investigations")
def get_investigations():

    return orchestrator.get_investigations()


# =====================================
# GET LATEST INVESTIGATION
# =====================================

@router.get("/api/investigations/latest")
def get_latest_investigation():

    investigations = orchestrator.get_investigations()

    if len(investigations) == 0:

        return {

            "message": "No investigations available"

        }

    return investigations[-1]


# =====================================
# CLEAR HISTORY
# =====================================

@router.delete("/api/investigations")
def clear_investigations():

    orchestrator.investigation_history.clear()

    return {

        "status": "success",

        "message": "Investigation history cleared"

    }