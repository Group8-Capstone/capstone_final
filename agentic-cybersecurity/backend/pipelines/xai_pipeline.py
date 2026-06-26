from explainability.shap_explainer import (
    generate_shap_plot
)

from explainability.lime_explainer import (
    generate_lime_plot
)

from explainability.feature_importance import (
    save_feature_importance
)

from explainability.permutation_importance import (
    save_permutation_importance
)


def run_xai_pipeline(

    model=None,

    X_train=None,

    X_sample=None,

    y_test=None,

    feature_names=None,

    importance_scores=None,

    model_name="fraud_detection"

):

    print("=" * 60)
    print("RUNNING XAI PIPELINE")
    print("=" * 60)

    try:

        # =====================================
        # SHAP
        # =====================================

        if (

            model is not None

            and X_sample is not None

        ):

            generate_shap_plot(

                model=model,

                X_sample=X_sample,

                feature_names=feature_names,

                model_name=model_name

            )

            print("SHAP explainability generated")

        # =====================================
        # LIME
        # =====================================

        if (

            model is not None

            and X_train is not None

            and X_sample is not None

        ):

            lime_train = X_train
            lime_sample = X_sample

            # CNN-LSTM / Transformer tensors
            if len(lime_train.shape) == 3:
                lime_train = lime_train.reshape(
                    lime_train.shape[0],
                    lime_train.shape[1]
                )

            if len(lime_sample.shape) == 3:
                lime_sample = lime_sample.reshape(
                    lime_sample.shape[0],
                    lime_sample.shape[1]
                )

            generate_lime_plot(
                model=model,
                X_train=lime_train,
                X_sample=lime_sample[0] if len(lime_sample.shape) > 1 else lime_sample,
                feature_names=feature_names,
                model_name=model_name
            )

            print("LIME explainability generated")

        # =====================================
        # FEATURE IMPORTANCE
        # =====================================

        if (

            feature_names is not None

            and importance_scores is not None

        ):

            save_feature_importance(

                feature_names,

                importance_scores

            )

            print("Feature importance generated")

        # =====================================
        # PERMUTATION IMPORTANCE
        # =====================================

        if (

            model is not None

            and X_sample is not None

            and y_test is not None

            and feature_names is not None

        ):

            save_permutation_importance(

                model=model,

                X_test=X_sample,

                y_test=y_test,

                feature_names=feature_names

            )

            print("Permutation importance generated")

        print("=" * 60)
        print("XAI PIPELINE COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"XAI pipeline error: {e}"
        )