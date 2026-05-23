from utils.save_attack_distribution import (
    save_attack_distribution
)

from utils.save_streaming_visualization import (
    save_streaming_visualization
)

from utils.save_lanl_visualization import (
    save_lanl_visualization
)

from utils.save_anomaly_visualization import (
    save_anomaly_visualization
)

from utils.save_ensemble_visualization import (
    save_ensemble_visualization
)

from utils.fraud_visualization import (
    save_fraud_chart
)


def run_visualization_pipeline(

    labels=None,

    fraud_predictions=None
):

    print("=" * 60)
    print("RUNNING VISUALIZATION PIPELINE")
    print("=" * 60)

    try:

        # =====================================
        # ATTACK DISTRIBUTION
        # =====================================

        if labels is not None:

            save_attack_distribution(
                labels
            )

            print(
                "Attack distribution generated"
            )

        # =====================================
        # STREAMING VISUALIZATION
        # =====================================

        save_streaming_visualization()

        print(
            "Streaming visualization generated"
        )

        # =====================================
        # ANOMALY VISUALIZATION
        # =====================================

        save_anomaly_visualization()

        print(
            "Anomaly visualization generated"
        )

        # =====================================
        # LANL VISUALIZATION
        # =====================================

        save_lanl_visualization()

        print(
            "LANL visualization generated"
        )

        # =====================================
        # ENSEMBLE VISUALIZATION
        # =====================================

        save_ensemble_visualization()

        print(
            "Ensemble visualization generated"
        )

        # =====================================
        # FRAUD VISUALIZATION
        # =====================================

        if fraud_predictions is not None:

            save_fraud_chart(
                fraud_predictions
            )

            print(
                "Fraud visualization generated"
            )

        print("=" * 60)
        print("VISUALIZATION PIPELINE COMPLETED")
        print("=" * 60)

    except Exception as e:

        print(
            f"Visualization pipeline error: {e}"
        )