from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing  import OneHotEncoder, StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin

numericals = ['amount_tsh', 'longitude', 'latitude', 'construction_year']
categoricals = ['region_code', 'scheme_management', 'quality_group', 'quantity_group', 'source', 'extraction_type_class', 'waterpoint_type']


class CustomTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.column_trans = None
#        self.ohe_col_names = None
    def fit(self, X_t, y_t = None):
        X_ = X_t.copy()
        column_transformer = ColumnTransformer(transformers = [('imputer', SimpleImputer(missing_values = 0.0, strategy = 'most_frequent'), ['construction_year']),
                                                      ('ohe', OneHotEncoder(sparse = False, handle_unknown = 'ignore'), categoricals)],
                                                      n_jobs = -1)
        column_transformer = column_transformer.fit(X_)
#        self.ohe_col_names = column_transformer.named_transformers_['ohe'].categories_[0]
        self.column_trans = column_transformer
        return column_transformer
    def transform(self, X, y = None):
        X_ = self.column_trans.transform(X)
        return X_
     
