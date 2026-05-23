import numpy as np

from agents.detection_agent import (
    DetectionAgent
)

from utils.logger import (
    log_message
)


class InferencePipeline:

    def __init__(self):

        self.detector = (
            DetectionAgent()
        )

    def run(self, data):

        result = self.detector.detect(
            data
        )

        return result


def run_inference_pipeline():

    print("=" * 60)
    print("RUNNING INFERENCE PIPELINE")
    print("=" * 60)

    try:

        # =====================================
        # SAMPLE INPUT DATA
        # =====================================

        sample_data = np.random.rand(
            10,
            78
        )

        # =====================================
        # RUN INFERENCE
        # =====================================

        pipeline = InferencePipeline()

        result = pipeline.run(
            sample_data
        )

        print(
            f"Inference Result: {result}"
        )

        log_message(
            "Inference pipeline completed"
        )

        print("=" * 60)
        print("INFERENCE PIPELINE COMPLETED")
        print("=" * 60)

        return result

    except Exception as e:

        print(
            f"Inference pipeline error: {e}"
        )

        log_message(
            f"Inference pipeline error: {e}"
        )

        return None