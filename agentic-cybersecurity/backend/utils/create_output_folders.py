import os


def create_output_folders():

    folders = [

        "outputs",

        "outputs/logs",

        "outputs/predictions",

        # =========================
        # Trained Models
        # =========================

        "outputs/trained_models",
        "outputs/trained_models/autoencoder",
        "outputs/trained_models/cnn_lstm",
        "outputs/trained_models/fraud_detection",
        "outputs/trained_models/lanl",
        "outputs/trained_models/transformer",

        # =========================
        # Explainability
        # =========================

        "outputs/explainability",
        "outputs/explainability/shap",
        "outputs/explainability/lime",
        "outputs/explainability/feature_importance",
        "outputs/explainability/permutation_importance",

        # =========================
        # Reports
        # =========================

        "outputs/reports",
        "outputs/reports/accuracy_plots",
        "outputs/reports/anomaly_reports",
        "outputs/reports/audit",
        "outputs/reports/classification_reports",
        "outputs/reports/confusion_matrix",
        "outputs/reports/ensemble",
        "outputs/reports/investigation",
        "outputs/reports/pipeline",
        "outputs/reports/response",
        "outputs/reports/roc_curves",

        # =========================
        # Visualizations
        # =========================

        "outputs/visualizations",
        "outputs/visualizations/anomaly_detection",
        "outputs/visualizations/attacks",
        "outputs/visualizations/ensemble",
        "outputs/visualizations/fraud",
        "outputs/visualizations/lanl",
        "outputs/visualizations/streaming",

        # Dashboard
        "dashboard"

    ]

    for folder in folders:

        os.makedirs(
            folder,
            exist_ok=True
        )

    print("=" * 60)
    print("OUTPUT FOLDERS CREATED SUCCESSFULLY")
    print("=" * 60)