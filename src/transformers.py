from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin

class CustomTransformer(BaseEstimator, TransformerMixin):
    
    
    def __init__(self):
        pass
    
    def fit(self, X, y = None):
        return self
    
    def transform(self, X, y = None):
        X_ = X.copy()
        column_transformer = ColumnTransformer(transformers = [('imputer', SimpleImputer(missing_values = 0.0, strategy = 'most_frequent'), ['construction_year']),                     
                                                      ('ohe', OneHotEncoder(sparse = False, handle_unknown = 'ignore'), categoricals),
                                                      ('scaler', StandardScaler(), numericals)], 
                                                      n_jobs = -1)
        X_new = column_transformer.fit_transform(X_)
        return X_new
     