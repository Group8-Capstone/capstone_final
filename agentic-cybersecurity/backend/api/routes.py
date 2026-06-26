from fastapi import (
    APIRouter,
    UploadFile,
    File
)

import numpy as np
import pandas as pd

from services.orchestrator_service import (
    run_pipeline
)

from streaming.websocket_manager import (
    websocket_manager
)

from services.dashboard_service import (
    get_dashboard_data
)


router = APIRouter()

# =====================================
# ROOT
# =====================================

@router.get("/")
def home():

    return {

        "message":

        "Agentic AI Cybersecurity Platform Running"
    }

# =====================================
# FILE UPLOAD
# =====================================

@router.post("/api/upload")
async def upload_file(

    file: UploadFile = File(...)
):

    content = await file.read()

    result = run_pipeline(
        content
    )

    return {

        "filename": file.filename,

        "status": "processed",

        "result": result
    }

# =====================================
# REAL LANL UEBA API
# =====================================

@router.get("/api/lanl-users")
def get_lanl_users():

    try:

        # =================================
        # LOAD LANL DATASET
        # =================================

        df = pd.read_csv(

            'datasets/lanl/auth.txt',

            header=None
        )

        # =================================
        # COLUMN NAMES
        # =================================

        df.columns = [

            'timestamp',

            'user',

            'computer'
        ]

        # =================================
        # USER ACTIVITY COUNT
        # =================================

        user_counts = (

            df.groupby('user')

            .size()

            .reset_index(name='count')
        )

        # =================================
        # UNIQUE SYSTEMS
        # =================================

        unique_systems = (

            df.groupby('user')['computer']

            .nunique()

            .reset_index(name='systems')
        )

        # =================================
        # MERGE
        # =================================

        result = pd.merge(

            user_counts,

            unique_systems,

            on='user'
        )

        # =================================
        # BETTER RISK SCORE
        # =================================

        result['risk'] = (

            np.log1p(result['count']) * 0.15 +

            result['systems'] * 0.03
        )

        # =================================
        # BETTER REASONS
        # =================================

        result['reason'] = result.apply(

            lambda row:

            'Privilege escalation'

            if row['systems'] > 50

            else (

                'High login frequency'

                if row['count'] > 500000

                else (

                    'Accessing multiple systems'

                    if row['risk'] > 1.1

                    else 'Normal behavior'
                )
            ),

            axis=1
        )

        # =================================
        # BETTER ACTIONS
        # =================================

        result['action'] = result['risk'].apply(

            lambda x:

            'Block'

            if x > 1.2

            else (

                'Investigate'

                if x > 0.9

                else 'Allow'
            )
        )

        # =================================
        # ROUND RISK
        # =================================

        result['risk'] = result['risk'].round(2)

        # =================================
        # SORT
        # =================================

        result = result.sort_values(

            by='risk',

            ascending=False
        )

        # =================================
        # RETURN TOP USERS
        # =================================

        return result.head(50).to_dict(

            orient='records'
        )

    except Exception as e:

        return {

            "error": str(e)
        }

# =====================================
# UEBA STATUS
# =====================================

@router.get("/api/ueba")
def ueba():

    return {

        "module": "UEBA",

        "status": "running",

        "active_users": 124,

        "anomalies_detected": 6
    }

# =====================================
# STREAMING STATUS
# =====================================

@router.get("/api/stream")
def stream():

    return {

        "stream": "active",

        "traffic_per_second": 2450,

        "alerts": 12
    }

# =====================================
# DASHBOARD METRICS
# =====================================

@router.get("/api/dashboard")
def dashboard_metrics():

    return get_dashboard_data()


# =====================================
# INCIDENT RESPONSE API
# =====================================

@router.get("/api/incident-response")
def incident_response():

    return [

        {
            "title": "Blocked IP Address",
            "description":
            "192.168.10.25 blocked due to DDoS activity",
            "status": "SUCCESS"
        },

        {
            "title": "Generated Alert",
            "description":
            "Critical malware behavior detected",
            "status": "ALERTED"
        },

        {
            "title": "Escalated Incident",
            "description":
            "SOC escalation initiated for insider threat",
            "status": "ESCALATED"
        },

        {
            "title": "Isolated Endpoint",
            "description":
            "Endpoint PC-104 isolated from network",
            "status": "ISOLATED"
        }
    ]

# =====================================
# INTRUSION DETECTION
# =====================================

@router.post("/predict/intrusion")
async def predict_intrusion():

    sample_prediction = np.random.choice(

        ['Normal', 'Attack']
    )

    confidence = round(

        np.random.uniform(
            0.85,
            0.99
        ),

        4
    )

    result = {

        "module": "Intrusion Detection",

        "prediction": sample_prediction,

        "confidence": confidence,

        "attack_type": "DDoS"
    }

    # =================================
    # LIVE ALERT
    # =================================

    if sample_prediction == 'Attack':

        await websocket_manager.broadcast({

            "type": "SECURITY_ALERT",

            "message":

            f"DDoS Attack Detected "
            f"(Confidence: {confidence})"
        })

    return result

# =====================================
# FRAUD DETECTION
# =====================================

@router.post("/predict/fraud")
async def predict_fraud():

    risk_score = round(

        np.random.uniform(
            0.80,
            0.99
        ),

        4
    )

    result = {

        "module": "Fraud Detection",

        "prediction": "Fraudulent Transaction",

        "risk_score": risk_score,

        "status": "HIGH_RISK"
    }

    # =================================
    # LIVE ALERT
    # =================================

    await websocket_manager.broadcast({

        "type": "FRAUD_ALERT",

        "message":

        f"Fraudulent transaction detected "
        f"(Risk: {risk_score})"
    })

    return result

# =====================================
# UEBA PREDICTION
# =====================================

@router.post("/predict/ueba")
async def predict_ueba():

    result = {

        "module": "UEBA",

        "anomaly_detected": True,

        "user": "EMP_104",

        "risk_level": "HIGH"
    }

    # =================================
    # LIVE ALERT
    # =================================

    await websocket_manager.broadcast({

        "type": "UEBA_ALERT",

        "message":

        "Suspicious insider activity detected "
        "for EMP_104"
    })

    return result

# =====================================
# AUTOENCODER ANOMALY
# =====================================

@router.post("/predict/anomaly")
async def predict_anomaly():

    anomaly_score = round(

        np.random.uniform(
            0.80,
            0.99
        ),

        4
    )

    result = {

        "module": "Autoencoder",

        "anomaly_score": anomaly_score,

        "threshold": 0.80,

        "status": "ANOMALY"
    }

    # =================================
    # LIVE ALERT
    # =================================

    await websocket_manager.broadcast({

        "type": "ANOMALY_ALERT",

        "message":

        f"Network anomaly detected "
        f"(Score: {anomaly_score})"
    })

    return result

# =====================================
# SIMULATE DDoS ATTACK
# =====================================

@router.post("/simulate/ddos")
async def simulate_ddos():

    packets = np.random.randint(
        10000,
        50000
    )

    result = {

        "simulation": "DDoS Attack",

        "status": "TRIGGERED",

        "packets_detected": packets
    }

    # =================================
    # LIVE ALERT
    # =================================

    await websocket_manager.broadcast({

        "type": "SECURITY_ALERT",

        "message":

        f"DDoS Attack Triggered "
        f"({packets} packets)"
    })

    return result

# =====================================
# SIMULATE PORT SCAN
# =====================================

@router.post("/simulate/portscan")
async def simulate_portscan():

    ports = np.random.randint(
        100,
        1000
    )

    result = {

        "simulation": "Port Scan",

        "status": "TRIGGERED",

        "ports_scanned": ports
    }

    await websocket_manager.broadcast({

        "type": "PORTSCAN_ALERT",

        "message":

        f"Port scan detected "
        f"({ports} ports scanned)"
    })

    return result

# =====================================
# SIMULATE MALWARE
# =====================================

@router.post("/simulate/malware")
async def simulate_malware():

    infected_hosts = np.random.randint(
        1,
        10
    )

    result = {

        "simulation": "Malware Activity",

        "status": "TRIGGERED",

        "infected_hosts": infected_hosts
    }

    await websocket_manager.broadcast({

        "type": "MALWARE_ALERT",

        "message":

        f"Malware activity detected "
        f"({infected_hosts} infected hosts)"
    })

    return result

# =====================================
# SHAP IMAGE
# =====================================

@router.get("/api/shap")
def get_shap():

    return {

        "title": "SHAP Explanation",

        "image":

        "http://127.0.0.1:8000/outputs/explainability/shap/shap_summary.png"
    }


# =====================================
# SHAP BAR IMAGE
# =====================================

@router.get("/api/shap-bar")
def get_shap_bar():

    return {

        "title": "SHAP Bar Plot",

        "image":

        "http://127.0.0.1:8000/outputs/explainability/shap/shap_bar.png"
    }


# =====================================
# LIME IMAGE
# =====================================

@router.get("/api/lime")
def get_lime():

    return {

        "title": "LIME Explanation",

        "image":

        "http://127.0.0.1:8000/outputs/explainability/lime/lime_explanation.png"
    }


# =====================================
# FEATURE IMPORTANCE
# =====================================

@router.get("/api/feature-importance")
def get_feature_importance():

    return {

        "title": "Feature Importance",

        "image":

        "http://127.0.0.1:8000/outputs/explainability/feature_importance/feature_importance.png"
    }


# =====================================
# PERMUTATION IMPORTANCE
# =====================================

@router.get("/api/permutation-importance")
def get_permutation_importance():

    return {

        "title": "Permutation Importance",

        "image":

        "http://127.0.0.1:8000/outputs/explainability/permutation_importance/permutation_importance.png"
    }


# =====================================
# CONFUSION MATRIX
# =====================================

@router.get("/api/confusion-matrix")
def get_confusion_matrix():

    return {

        "title": "Confusion Matrix",

        "image":

        "http://127.0.0.1:8000/outputs/reports/confusion_matrix/model_cm.png"
    }


# =====================================
# ROC CURVE
# =====================================

@router.get("/api/roc")
def get_roc():

    return {

        "title": "ROC Curve",

        "image":

        "http://127.0.0.1:8000/outputs/reports/roc_curves/model_roc.png"
    }


# =====================================
# TRAINING ACCURACY
# =====================================

@router.get("/api/training-accuracy")
def get_training_accuracy():

    return {

        "title": "Training Accuracy",

        "image":

        "http://127.0.0.1:8000/outputs/reports/accuracy_plots/model_accuracy.png"
    }


# =====================================
# TRAINING LOSS
# =====================================

@router.get("/api/training-loss")
def get_training_loss():

    return {

        "title": "Training Loss",

        "image":

        "http://127.0.0.1:8000/outputs/reports/accuracy_plots/model_loss.png"
    }