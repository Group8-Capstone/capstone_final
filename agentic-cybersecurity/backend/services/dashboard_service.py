import json
from pathlib import Path
from collections import Counter

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUTS = BASE_DIR / "outputs"
DASHBOARD = BASE_DIR / "dashboard"


def _count_files(path: Path):
    return sum(1 for p in path.rglob("*") if p.is_file()) if path.exists() else 0


def _read_prediction_counts():

    pred_dir = OUTPUTS / "predictions"

    total = 0
    fraud = 0

    attack_counter = Counter()

    if pred_dir.exists():

        for csv in pred_dir.glob("*.csv"):

            try:

                import pandas as pd

                df = pd.read_csv(csv)

                total += len(df)

                if "prediction" in df.columns:
                    fraud += int((df["prediction"] == 1).sum())

                if "attack_type" in df.columns:
                    attack_counter.update(
                        df["attack_type"].astype(str)
                    )

            except Exception:
                pass

    return total, fraud, attack_counter


# ==========================================================
# MODEL ACCURACY
# ==========================================================

def _model_accuracy():

    results = []

    tm = OUTPUTS / "trained_models"

    if not tm.exists():
        return results

    supported_models = {

        "cnn_lstm",

        "transformer",

        "fraud_detection"

    }

    for model in tm.iterdir():

        if model.name.startswith("."):
            continue

        if not model.is_dir():
            continue

        if model.name not in supported_models:
            continue

        metric_file = model / "metrics.json"

        accuracy = 0

        if metric_file.exists():

            try:

                with open(metric_file, "r") as f:
                    metrics = json.load(f)

                accuracy = metrics.get(
                    "accuracy",
                    0
                )

            except Exception:
                accuracy = 0

        results.append({

            "model": model.name,

            "accuracy": round(
                float(accuracy),
                2
            )

        })

    return results


# ==========================================================
# AUTOENCODER
# ==========================================================

def _autoencoder_metrics():

    metric_file = (
        OUTPUTS
        / "trained_models"
        / "autoencoder"
        / "metrics.json"
    )

    if metric_file.exists():

        try:

            with open(metric_file, "r") as f:
                return json.load(f)

        except Exception:
            pass

    return {}


# ==========================================================
# LANL
# ==========================================================

def _lanl_metrics():

    metric_file = (
        OUTPUTS
        / "trained_models"
        / "lanl"
        / "metrics.json"
    )

    if metric_file.exists():

        try:

            with open(metric_file, "r") as f:
                return json.load(f)

        except Exception:
            pass

    return {}


# ==========================================================
# DASHBOARD
# ==========================================================

def get_dashboard_data():

    total_predictions, fraud_alerts, attacks = (
        _read_prediction_counts()
    )

    metrics = {

        "total_threats": total_predictions,

        "blocked_attacks": max(
            total_predictions - fraud_alerts,
            0
        ),

        "fraud_alerts": fraud_alerts,

        "ueba_alerts": _count_files(
            OUTPUTS / "reports" / "anomaly_reports"
        ),

        "system_health": "Healthy"

    }

    traffic = [

        {
            "time": f"T{i+1}",
            "traffic": value
        }

        for i, value in enumerate(

            [

                20,

                35,

                28,

                42,

                39,

                55,

                48,

                total_predictions

            ]

        )

    ]

    attack_distribution = (

        [

            {

                "name": k,

                "value": v

            }

            for k, v in attacks.items()

        ]

        if attacks

        else

        [

            {

                "name": "Normal",

                "value": max(

                    total_predictions - fraud_alerts,

                    0

                )

            },

            {

                "name": "Fraud",

                "value": fraud_alerts

            }

        ]

    )

    return {

        "metrics": metrics,

        "traffic": traffic,

        "attack_distribution": attack_distribution,

        "model_accuracy": _model_accuracy(),

        # NEW
        "autoencoder": _autoencoder_metrics(),

        "lanl": _lanl_metrics(),

        "system": {

            "trained_models": _count_files(
                OUTPUTS / "trained_models"
            ),

            "reports_generated": _count_files(
                OUTPUTS / "reports"
            ),

            "visualizations_generated": _count_files(
                OUTPUTS / "visualizations"
            ),

            "explainability_outputs": _count_files(
                OUTPUTS / "explainability"
            ),

            "prediction_outputs": _count_files(
                OUTPUTS / "predictions"
            )

        }

    }