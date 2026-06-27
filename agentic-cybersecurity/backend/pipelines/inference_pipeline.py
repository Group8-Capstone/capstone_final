import numpy as np

from agents.detection_agent import DetectionAgent
from utils.logger import log_message


class InferencePipeline:

    def __init__(self):

        self.detector = DetectionAgent()

    # =====================================================
    # RUN INFERENCE
    # =====================================================

    def run(self, data):

        if data is None:

            raise ValueError(
                "Input data cannot be None"
            )

        if not isinstance(data, np.ndarray):

            data = np.array(data)

        data = data.astype(np.float32)

        return self.detector.detect(data)


# =====================================================
# PIPELINE ENTRY
# =====================================================

def run_inference_pipeline(input_data=None):

    print("=" * 60)
    print("RUNNING INFERENCE PIPELINE")
    print("=" * 60)

    try:

        if input_data is None:

            print("No input provided.")
            print("Using sample CICIDS data.")

            input_data = np.random.rand(
                10,
                78
            ).astype(np.float32)

        pipeline = InferencePipeline()

        result = pipeline.run(input_data)

        print()

        print("Inference Result")

        print(result)

        log_message(
            "Inference pipeline completed"
        )

        print("=" * 60)
        print("INFERENCE PIPELINE COMPLETED")
        print("=" * 60)

        return result

    except Exception as e:

        print(
            f"Inference Pipeline Error : {e}"
        )

        log_message(
            f"Inference pipeline error : {e}"
        )

        return None