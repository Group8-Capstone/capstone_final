import numpy as np

from agents.detection_agent import DetectionAgent
from services.model_initializer import get_model
from utils.logger import log_message


class InferencePipeline:

    def __init__(self):

        self.cnn_model = get_model("cnn_lstm")
        self.transformer_model = get_model("transformer")
        self.detector = DetectionAgent(
            cnn_model=self.cnn_model,
            transformer_model=self.transformer_model
        )

    def run(self, data):

        if data is None:
            raise Exception("Input data cannot be None")

        if not isinstance(data, np.ndarray):
            data = np.array(data)

        return self.detector.detect(data)


def run_inference_pipeline(input_data=None):

    print("=" * 60)
    print("RUNNING INFERENCE PIPELINE")
    print("=" * 60)

    try:

        if input_data is None:

            print("No input provided.")
            print("Using sample input for pipeline verification.")

            input_data = np.random.rand(10, 78).astype(np.float32)

        pipeline = InferencePipeline()

        result = pipeline.run(input_data)

        print(f"Inference Result : {result}")

        log_message("Inference pipeline completed")

        print("=" * 60)
        print("INFERENCE PIPELINE COMPLETED")
        print("=" * 60)

        return result

    except Exception as e:

        print(f"Inference Pipeline Error : {e}")

        log_message(f"Inference pipeline error : {e}")

        return None