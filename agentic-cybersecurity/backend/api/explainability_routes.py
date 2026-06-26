import os

from fastapi import APIRouter

router = APIRouter(
    tags=["Explainability"]
)

BASE_URL = "http://127.0.0.1:8000"

# =====================================================
# HELPER
# =====================================================

def get_image(relative_path):

    full_path = os.path.join(
        "outputs",
        relative_path
    )

    if os.path.exists(full_path):

        return {
            "available": True,
            "image": f"{BASE_URL}/outputs/{relative_path}"
        }

    return {
        "available": False,
        "image": None
    }


# =====================================================
# SHAP SUMMARY
# =====================================================

@router.get("/api/shap")
def shap():

    return get_image(
        "explainability/shap/shap_summary.png"
    )


# =====================================================
# SHAP BAR
# =====================================================

@router.get("/api/shap-bar")
def shap_bar():

    return get_image(
        "explainability/shap/shap_bar.png"
    )


# =====================================================
# LIME
# =====================================================

@router.get("/api/lime")
def lime():

    return get_image(
        "explainability/lime/lime_explanation.png"
    )


# =====================================================
# FEATURE IMPORTANCE
# =====================================================

@router.get("/api/feature-importance")
def feature_importance():

    return get_image(
        "explainability/feature_importance/feature_importance.png"
    )


# =====================================================
# PERMUTATION IMPORTANCE
# =====================================================

@router.get("/api/permutation-importance")
def permutation_importance():

    return get_image(
        "explainability/permutation_importance/permutation_importance.png"
    )


# =====================================================
# ROC CURVE
# =====================================================

@router.get("/api/roc")
def roc():

    return get_image(
        "reports/roc_curves/model_roc.png"
    )


# =====================================================
# CONFUSION MATRIX
# =====================================================

@router.get("/api/confusion-matrix")
def confusion_matrix():

    return get_image(
        "reports/confusion_matrix/model_cm.png"
    )


# =====================================================
# NORMALIZED CONFUSION MATRIX
# =====================================================

@router.get("/api/confusion-matrix-normalized")
def normalized_confusion():

    return get_image(
        "reports/confusion_matrix/model_normalized_cm.png"
    )


# =====================================================
# HEATMAP CONFUSION MATRIX
# =====================================================

@router.get("/api/confusion-matrix-heatmap")
def heatmap():

    return get_image(
        "reports/confusion_matrix/model_heatmap.png"
    )


# =====================================================
# TRAINING CURVE
# =====================================================

@router.get("/api/training")
def training_curve():

    return get_image(
        "training_plots/cnn_lstm_training.png"
    )


# =====================================================
# ALL EXPLAINABILITY OUTPUTS
# =====================================================

@router.get("/api/explainability")
def explainability():

    return {

        "shap":

        get_image(
            "explainability/shap/shap_summary.png"
        ),

        "shap_bar":

        get_image(
            "explainability/shap/shap_bar.png"
        ),

        "lime":

        get_image(
            "explainability/lime/lime_explanation.png"
        ),

        "feature_importance":

        get_image(
            "explainability/feature_importance/feature_importance.png"
        ),

        "permutation_importance":

        get_image(
            "explainability/permutation_importance/permutation_importance.png"
        ),

        "roc":

        get_image(
            "reports/roc_curves/model_roc.png"
        ),

        "confusion_matrix":

        get_image(
            "reports/confusion_matrix/model_cm.png"
        )

    }