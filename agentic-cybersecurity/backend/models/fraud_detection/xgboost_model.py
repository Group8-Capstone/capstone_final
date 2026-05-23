import joblib
import xgboost as xgb
import numpy as np

from sklearn.model_selection import (
    train_test_split
)

from sklearn.preprocessing import (
    StandardScaler
)

from sklearn.metrics import (
    accuracy_score,
    classification_report
)

from utils.save_confusion_matrix import (
    save_confusion_matrix
)

from utils.fraud_visualization import (
    save_fraud_chart
)

from utils.save_classification_report import (
    save_classification_report
)

from utils.save_roc_curve import (
    save_roc_curve
)

from utils.save_predictions import (
    save_predictions
)

from explainability.shap_explainer import (
    generate_shap_plot
)

from explainability.feature_importance import (
    save_feature_importance
)


class FraudDetectionModel:

    def __init__(self):

        print("=" * 60)
        print("INITIALIZING FRAUD MODEL")
        print("=" * 60)

        self.scaler = StandardScaler()

        self.model = xgb.XGBClassifier(

            n_estimators=150,

            max_depth=6,

            learning_rate=0.05,

            subsample=0.8,

            colsample_bytree=0.8,

            objective='binary:logistic',

            eval_metric='logloss',

            random_state=42,

            n_jobs=-1
        )

    def train(self, df):

        print("=" * 60)
        print("STARTING FRAUD DETECTION TRAINING")
        print("=" * 60)

        # =====================================
        # HANDLE NULL VALUES
        # =====================================

        df = df.fillna(0)

        print(
            f"Dataset Shape: {df.shape}"
        )

        # =====================================
        # FEATURES / LABELS
        # =====================================

        X = df.drop(
            'Class',
            axis=1
        )

        y = df['Class']

        print(
            f"Feature Shape: {X.shape}"
        )

        print(
            f"Label Distribution:\n"
            f"{y.value_counts()}"
        )

        # =====================================
        # FEATURE SCALING
        # =====================================

        X = self.scaler.fit_transform(X)

        print(
            "Feature scaling completed"
        )

        # =====================================
        # TRAIN TEST SPLIT
        # =====================================

        X_train, X_test, y_train, y_test = (

            train_test_split(

                X,

                y,

                test_size=0.2,

                random_state=42,

                stratify=y
            )
        )

        print(
            f"Train Shape: {X_train.shape}"
        )

        print(
            f"Test Shape: {X_test.shape}"
        )

        # =====================================
        # MODEL TRAINING
        # =====================================

        print("=" * 60)
        print("TRAINING XGBOOST MODEL")
        print("=" * 60)

        self.model.fit(

            X_train,

            y_train
        )

        print(
            "Training completed"
        )

        # =====================================
        # PREDICTIONS
        # =====================================

        predictions = self.model.predict(
            X_test
        )

        prediction_probabilities = (

            self.model.predict_proba(
                X_test
            )[:, 1]
        )

        # =====================================
        # EVALUATION
        # =====================================

        accuracy = accuracy_score(

            y_test,

            predictions
        )

        print(
            f"Fraud Detection Accuracy: "
            f"{accuracy}"
        )

        report = classification_report(

            y_test,

            predictions,

            zero_division=0
        )

        print(report)

        # =====================================
        # SAVE CLASSIFICATION REPORT
        # =====================================

        save_classification_report(

            y_test,

            predictions,

            'fraud_detection'
        )

        # =====================================
        # SAVE ROC CURVE
        # =====================================

        save_roc_curve(

            y_test,

            prediction_probabilities,

            'fraud_detection'
        )

        # =====================================
        # SAVE PREDICTIONS
        # =====================================

        save_predictions(

            predictions,

            'fraud_detection'
        )

        # =====================================
        # SAVE CONFUSION MATRIX
        # =====================================

        save_confusion_matrix(

            y_test,

            predictions,

            'fraud_detection'
        )

        # =====================================
        # FRAUD VISUALIZATION
        # =====================================

        save_fraud_chart(
            predictions
        )

        # =====================================
        # SHAP EXPLAINABILITY
        # =====================================

        try:

            generate_shap_plot(

                self.model,

                X_test
            )

        except Exception as e:

            print(
                f"SHAP generation failed: {e}"
            )

        # =====================================
        # FEATURE IMPORTANCE
        # =====================================

        try:

            feature_names = [

                f'Feature_{i}'

                for i in range(
                    X_train.shape[1]
                )
            ]

            importance_scores = (
                self.model.feature_importances_
            )

            save_feature_importance(

                feature_names,

                importance_scores
            )

        except Exception as e:

            print(
                f"Feature importance "
                f"generation failed: {e}"
            )

        # =====================================
        # SAVE MODEL
        # =====================================

        model_path = (

            'outputs/trained_models/'
            'fraud_detection/fraud_model.pkl'
        )

        scaler_path = (

            'outputs/trained_models/'
            'fraud_detection/scaler.pkl'
        )

        joblib.dump(

            self.model,

            model_path
        )

        joblib.dump(

            self.scaler,

            scaler_path
        )

        print("=" * 60)
        print("FRAUD MODEL SAVED SUCCESSFULLY")
        print("=" * 60)

        print(
            f"Model Path: {model_path}"
        )

        print(
            f"Scaler Path: {scaler_path}"
        )

        return accuracy

    def predict(self, data):

        scaled_data = self.scaler.transform(
            data
        )

        prediction = self.model.predict(
            scaled_data
        )

        probability = (
            self.model.predict_proba(
                scaled_data
            )
        )

        return {

            'prediction':
            prediction.tolist(),

            'probability':
            probability.tolist()
        }