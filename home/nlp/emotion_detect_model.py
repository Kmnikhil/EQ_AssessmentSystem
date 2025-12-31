from transformers import pipeline

class EmotionAnalyzer:
    _model = None

    @classmethod
    def load_model(cls):
        if cls._model is None:
            cls._model = pipeline(
                "text-classification",
                model="j-hartmann/emotion-english-distilroberta-base",
                return_all_scores=True
            )
        return cls._model
