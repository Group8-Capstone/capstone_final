from services.dataset_router import get_dataset_processor


class TrainPipeline:

    def __init__(self, dataset_name, dataset_path):

        self.dataset_name = dataset_name
        self.dataset_path = dataset_path

    def run(self):

        processor = get_dataset_processor(self.dataset_name)

        df = processor(self.dataset_path)

        print(df.head())

        return {
            "status": "training_started",
            "dataset": self.dataset_name
        }