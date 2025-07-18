"""
Model training and prediction interfaces for AI-Enhanced Analysis.
"""
import joblib

class ModelClient:
    """
    Load and use trained ML models for predictions.
    """
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, features_df):
        """
        Predict labels or scores for a DataFrame of features.
        """
        return self.model.predict(features_df)

    def predict_proba(self, features_df):
        """
        Predict probability scores for classification models.
        """
        if hasattr(self.model, 'predict_proba'):
            return self.model.predict_proba(features_df)
        raise AttributeError('Model does not support probability estimates')
