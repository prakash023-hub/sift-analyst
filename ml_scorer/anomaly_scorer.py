import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

class LogAnomalyScorer:
    """
    ML-based pre-filter for forensic log analysis.
    Inspired by PK/PD outlier detection — anomalies in 
    drug concentration curves = anomalies in system behavior.
    """
    def __init__(self, contamination=0.1):
        self.model = IsolationForest(contamination=contamination, random_state=42)
        self.scaler = StandardScaler()

    def score_events(self, events):
        if not events:
            return []
        df = pd.DataFrame(events)
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        df['is_night'] = ((df['hour'] >= 22) | (df['hour'] <= 5)).astype(int)
        df['log_size'] = np.log1p(df.get('size', 0))
        features = df[['hour', 'is_night', 'log_size']].fillna(0)
        X = self.scaler.fit_transform(features)
        scores = self.model.fit_predict(X)
        df['is_evil'] = (scores == -1).astype(int)
        df['anomaly_score'] = self.model.score_samples(X)
        suspicious = df[df['is_evil'] == 1].sort_values('anomaly_score')
        return suspicious.to_dict('records')
