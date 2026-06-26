from fastapi import APIRouter
import pandas as pd
import numpy as np
import os
import json

router = APIRouter(
    tags=["LANL UEBA"]
)

DATASET = "datasets/lanl/auth.txt"
MODEL_DIR = "outputs/trained_models/lanl"


# =====================================================
# LANL USER ANALYTICS
# =====================================================

@router.get("/api/lanl-users")
def lanl_users():

    try:

        df = pd.read_csv(
            DATASET,
            header=None
        )

        df.columns = [

            "timestamp",

            "user",

            "computer"

        ]

        ###################################################

        user_count = (

            df.groupby("user")

            .size()

            .reset_index(name="login_count")

        )

        ###################################################

        systems = (

            df.groupby("user")["computer"]

            .nunique()

            .reset_index(name="systems")

        )

        ###################################################

        result = pd.merge(

            user_count,

            systems,

            on="user"

        )

        ###################################################

        result["risk"] = (

            np.log1p(result["login_count"]) * 0.15 +

            result["systems"] * 0.03

        )

        ###################################################

        def reason(row):

            if row["systems"] > 50:

                return "Privilege Escalation"

            elif row["login_count"] > 500000:

                return "High Login Frequency"

            elif row["risk"] > 1.2:

                return "Multiple System Access"

            return "Normal"

        ###################################################

        def action(score):

            if score > 1.3:

                return "Block"

            elif score > 1.0:

                return "Investigate"

            return "Allow"

        ###################################################

        result["reason"] = result.apply(

            reason,

            axis=1

        )

        result["action"] = result["risk"].apply(

            action

        )

        result["risk"] = result["risk"].round(2)

        ###################################################

        result = result.sort_values(

            "risk",

            ascending=False

        )

        return result.head(50).to_dict(

            orient="records"

        )

    except Exception as e:

        return {

            "error": str(e)

        }


# =====================================================
# UEBA DASHBOARD
# =====================================================

@router.get("/api/ueba")
def ueba_dashboard():

    try:

        df = pd.read_csv(

            DATASET,

            header=None

        )

        df.columns = [

            "timestamp",

            "user",

            "computer"

        ]

        users = df["user"].nunique()

        systems = df["computer"].nunique()

        events = len(df)

        anomalies = int(events * 0.02)

        return {

            "module": "UEBA",

            "status": "Running",

            "active_users": users,

            "systems": systems,

            "events": events,

            "estimated_anomalies": anomalies

        }

    except Exception as e:

        return {

            "error": str(e)

        }


# =====================================================
# LANL METRICS
# =====================================================

@router.get("/api/lanl-metrics")
def lanl_metrics():

    metrics_file = os.path.join(

        MODEL_DIR,

        "metrics.json"

    )

    if os.path.exists(metrics_file):

        with open(

            metrics_file,

            "r"

        ) as f:

            return json.load(f)

    return {

        "model": "Isolation Forest",

        "status": "Available",

        "accuracy": 0,

        "anomaly_rate": 0

    }


# =====================================================
# TOP RISK USERS
# =====================================================

@router.get("/api/lanl-top-users")
def top_users():

    users = lanl_users()

    if isinstance(users, dict):

        return users

    return users[:10]


# =====================================================
# MODEL STATUS
# =====================================================

@router.get("/api/lanl-model")
def lanl_model():

    model_path = os.path.join(

        MODEL_DIR,

        "lanl_model.pkl"

    )

    feature_path = os.path.join(

        MODEL_DIR,

        "feature_names.pkl"

    )

    metrics_path = os.path.join(

        MODEL_DIR,

        "metrics.json"

    )

    return {

        "trained":

        os.path.exists(model_path),

        "features":

        os.path.exists(feature_path),

        "metrics":

        os.path.exists(metrics_path)

    }