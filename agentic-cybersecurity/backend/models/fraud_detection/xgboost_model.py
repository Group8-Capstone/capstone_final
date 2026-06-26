import joblib
import xgboost as xgb

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

from utils.save_confusion_matrix import save_confusion_matrix
from utils.fraud_visualization import save_fraud_chart
from utils.save_classification_report import save_classification_report
from utils.save_roc_curve import save_roc_curve
from utils.save_predictions import save_predictions

from explainability.shap_explainer import generate_shap_plot
from explainability.lime_explainer import generate_lime_plot
from explainability.feature_importance import save_feature_importance
from explainability.permutation_importance import save_permutation_importance


class FraudDetectionModel:

    def __init__(self):

        self.scaler = StandardScaler()

        try:
            self.feature_names = joblib.load(
                "outputs/trained_models/fraud_detection/feature_names.pkl"
            )
        except Exception:
            self.feature_names = None

        self.model = xgb.XGBClassifier(
            n_estimators=150,
            max_depth=6,
            learning_rate=0.05,
            subsample=0.8,
            colsample_bytree=0.8,
            objective="binary:logistic",
            eval_metric="logloss",
            random_state=42,
            n_jobs=-1,
        )

    def train(self, df):

        df = df.fillna(0)

        X = df.drop("Class", axis=1)

        # Dynamic feature names
        feature_names = X.columns.tolist()

        y = df["Class"]

        X = self.scaler.fit_transform(X)

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y,
        )

        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)
        probabilities = self.model.predict_proba(X_test)[:, 1]

        accuracy = accuracy_score(y_test, predictions)

        print(classification_report(
            y_test,
            predictions,
            zero_division=0
        ))

        save_classification_report(
            y_test,
            predictions,
            "fraud_detection"
        )

        save_roc_curve(
            y_test,
            probabilities,
            "fraud_detection"
        )

        save_predictions(
            predictions,
            "fraud_detection"
        )

        save_confusion_matrix(
            y_test,
            predictions,
            "fraud_detection"
        )

        save_fraud_chart(predictions)

        try:
            generate_shap_plot(
                self.model,
                X_test,
                feature_names
            )
        except Exception as e:
            print(e)

        try:
            generate_lime_plot(
                self.model,
                X_train,
                X_test[0],
                "fraud_detection"
            )
        except Exception as e:
            print(e)

        try:
            save_feature_importance(
                feature_names,
                self.model.feature_importances_
            )
        except Exception as e:
            print(e)

    
        try:
            save_permutation_importance(
                self.model,
                X_test,
                y_test,
                feature_names,
                "fraud_detection"
            )
        except Exception as e:
            print(e)

        model_path = "outputs/trained_models/fraud_detection/fraud_model.pkl"
        scaler_path = "outputs/trained_models/fraud_detection/scaler.pkl"
        feature_path = "outputs/trained_models/fraud_detection/feature_names.pkl"

        joblib.dump(self.model, model_path)
        joblib.dump(self.scaler, scaler_path)
        joblib.dump(feature_names, feature_path)

        self.feature_names = feature_names

        return accuracy

    def predict(self, data):

        scaled = self.scaler.transform(data)

        prediction = self.model.predict(scaled)
        probability = self.model.predict_proba(scaled)

        return {
            "prediction": prediction.tolist(),
            "probability": probability.tolist()
        }
