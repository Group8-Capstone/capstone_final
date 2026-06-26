from fastapi import APIRouter

# =====================================================
# IMPORT ROUTERS
# =====================================================

from api.dashboard_routes import (
    router as dashboard_router
)

from api.prediction_routes import (
    router as prediction_router
)

from api.investigation_routes import (
    router as investigation_router
)

from api.incident_routes import (
    router as incident_router
)

from api.explainability_routes import (
    router as explainability_router
)

from api.streaming_routes import (
    router as streaming_router
)

from api.lanl_routes import (
    router as lanl_router
)

# =====================================================
# MAIN ROUTER
# =====================================================

router = APIRouter()

# =====================================================
# ROOT
# =====================================================

@router.get(
    "/",
    tags=["System"]
)
def home():

    return {

        "application":
        "Agentic AI Cybersecurity Threat Detection",

        "version":
        "1.0",

        "status":
        "Running"

    }


# =====================================================
# REGISTER ROUTERS
# =====================================================

router.include_router(
    dashboard_router
)

router.include_router(
    prediction_router
)

router.include_router(
    investigation_router
)

router.include_router(
    incident_router
)

router.include_router(
    explainability_router
)

router.include_router(
    streaming_router
)

router.include_router(
    lanl_router
)