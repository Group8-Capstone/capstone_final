from fastapi import APIRouter

from services.dashboard_service import (
    get_dashboard_data
)

router = APIRouter(
    tags=["Dashboard"]
)


# =====================================================
# DASHBOARD METRICS
# =====================================================

@router.get("/api/dashboard")
def dashboard():

    return get_dashboard_data()


# =====================================================
# DASHBOARD HEALTH
# =====================================================

@router.get("/api/dashboard/health")
def dashboard_health():

    data = get_dashboard_data()

    return {

        "status": "running",

        "system_health": data["metrics"]["system_health"],

        "trained_models": data["system"]["trained_models"],

        "reports_generated": data["system"]["reports_generated"],

        "prediction_outputs": data["system"]["prediction_outputs"]

    }


# =====================================================
# DASHBOARD MODEL METRICS
# =====================================================

@router.get("/api/dashboard/models")
def model_metrics():

    data = get_dashboard_data()

    return data["model_accuracy"]


# =====================================================
# DASHBOARD ATTACK DISTRIBUTION
# =====================================================

@router.get("/api/dashboard/attacks")
def attack_distribution():

    data = get_dashboard_data()

    return data["attack_distribution"]


# =====================================================
# DASHBOARD TRAFFIC
# =====================================================

@router.get("/api/dashboard/traffic")
def traffic():

    data = get_dashboard_data()

    return data["traffic"]


# =====================================================
# DASHBOARD SYSTEM INFO
# =====================================================

@router.get("/api/dashboard/system")
def system_information():

    data = get_dashboard_data()

    return data["system"]