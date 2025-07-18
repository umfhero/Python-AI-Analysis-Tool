"""
Feature extraction for ML workflows.
"""
import pandas as pd


def extract_features(findings):
    """
    Convert AST findings and code metrics into a pandas DataFrame for ML.
    """
    records = [f.to_dict() for f in findings]
    df = pd.DataFrame(records)
    return df
