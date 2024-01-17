import cohere
from cohere_config import co  # Make sure cohere_config.py is set up correctly


class Classifier:
    def __init__(self, model_name='single-label-ft'):
        self.model_name = model_name
        self.finetuned_classifier = self.load_model()

    def load_model(self):
        # Retrieve and return the custom model from Cohere
        return co.get_custom_model_by_name(self.model_name)

    def classify(self, query):
        # Use the Cohere classify endpoint with the custom model to classify the query
        response = co.classify(
            inputs=[query],
            model=self.finetuned_classifier.model_id,
        )
        return response[0].predictions[0]
