from fastapi import APIRouter
import numpy as np

from services.orchestrator_service import run_pipeline
from streaming.websocket_manager import websocket_manager

router = APIRouter(
    tags=["Prediction"]
)


# =====================================================
# INTRUSION DETECTION
# =====================================================

@router.post("/predict/intrusion")
async def predict_intrusion():

    sample = np.random.rand(10, 78).astype(np.float32)

    result = run_pipeline(sample)

    detection = result["detection"]

    await websocket_manager.broadcast({

        "type": "SECURITY_ALERT",

        "attack_type": detection["attack_type"],

        "severity": detection["severity"],

        "score": detection["score"],

        "message":
        f'{detection["attack_type"]} detected '
        f'({detection["score"]:.4f})'

    })

    return result


# =====================================================
# FRAUD DETECTION
# =====================================================

@router.post("/predict/fraud")
async def predict_fraud():

    sample = np.random.rand(1, 30).astype(np.float32)

    result = run_pipeline(sample)

    await websocket_manager.broadcast({

        "type": "FRAUD_ALERT",

        "message": "Fraud Detection Completed"

    })

    return result


# =====================================================
# UEBA
# =====================================================

@router.post("/predict/ueba")
async def predict_ueba():

    sample = np.random.rand(20, 3)

    result = run_pipeline(sample)

    await websocket_manager.broadcast({

        "type": "UEBA_ALERT",

        "message": "UEBA Analysis Completed"

    })

    return result


# =====================================================
# AUTOENCODER ANOMALY
# =====================================================

@router.post("/predict/anomaly")
async def predict_anomaly():

    sample = np.random.rand(10, 78).astype(np.float32)

    result = run_pipeline(sample)

    await websocket_manager.broadcast({

        "type": "ANOMALY_ALERT",

        "message": "Anomaly Detection Completed"

    })

    return result