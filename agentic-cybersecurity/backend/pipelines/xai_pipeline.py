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

        if model is not None and X_sample is not None:

            generate_shap_plot(

                model=model,

                X_sample=X_sample,

                feature_names=feature_names,

                model_name=model_name

            )

            print(
                "SHAP explainability generated"
            )

        # =====================================
        # LIME
        # =====================================

        if (

            model is not None

            and X_train is not None

            and X_sample is not None

        ):

            generate_lime_plot(

                model=model,

                X_train=X_train,

                X_sample=X_sample[0]

                if len(X_sample.shape) > 1

                else X_sample,

                model_name=model_name

            )

            print(
                "LIME explainability generated"
            )

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

            print(
                "Feature importance generated"
            )

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

                model,

                X_sample,

                y_test,

                feature_names

            )

            print(
                "Permutation importance generated"
            )

        print("=" * 60)
        print("XAI PIPELINE COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"XAI pipeline error: {e}"
        )