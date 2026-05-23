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

    X_sample=None,

    feature_names=None,

    importance_scores=None
):

    print("=" * 60)
    print("RUNNING XAI PIPELINE")
    print("=" * 60)

    try:

        # =====================================
        # SHAP
        # =====================================

        generate_shap_plot(

            model,

            X_sample
        )

        print(
            "SHAP explainability generated"
        )

        # =====================================
        # LIME
        # =====================================

        generate_lime_plot()

        print(
            "LIME explainability generated"
        )

        # =====================================
        # FEATURE IMPORTANCE
        # =====================================

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

        save_permutation_importance()

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