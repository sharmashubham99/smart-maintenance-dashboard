import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier

class ModelExplainability:
    def __init__(self, model):
        self.model = model
        self.feature_names = None

    def set_feature_names(self, feature_names):
        self.feature_names = feature_names

    def get_feature_importance(self):
        """Extract feature importance from the trained model"""
        if hasattr(self.model, 'feature_importances_'):
            importances = self.model.feature_importances_
            return importances
        else:
            raise ValueError("Model does not support feature importance extraction")

    def plot_feature_importance(self, top_n=10):
        """Plot feature importance visualization"""
        importances = self.get_feature_importance()
        
        # Sort features by importance
        indices = np.argsort(importances)[::-1][:top_n]
        
        # Create plot
        plt.figure(figsize=(10, 6))
        plt.title("Feature Importance for Machine Failure Prediction")
        plt.bar(range(len(indices)), importances[indices])
        
        if self.feature_names:
            plt.xticks(range(len(indices)), 
                       [self.feature_names[i] for i in indices], 
                       rotation=45, ha='right')
        else:
            plt.xticks(range(len(indices)), 
                       [f"Feature {i}" for i in indices], 
                       rotation=45, ha='right')
        
        plt.ylabel("Importance")
        plt.tight_layout()
        return plt

    def explain_prediction(self, sample, prediction_proba):
        """Generate explanation for a specific prediction"""
        importances = self.get_feature_importance()
        
        explanation = {
            "prediction": prediction_proba[1] * 100,  # Failure probability in percentage
            "top_factors": []
        }
        
        # Get top contributing features
        top_indices = np.argsort(importances)[::-1][:3]
        for idx in top_indices:
            factor_name = self.feature_names[idx] if self.feature_names else f"Feature {idx}"
            explanation["top_factors"].append({
                "feature": factor_name,
                "importance": importances[idx] * 100,
                "value": sample[idx]
            })
        
        return explanation