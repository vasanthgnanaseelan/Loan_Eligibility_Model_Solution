# modules/model.py

import pandas as pd
import pickle
import logging
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

def train_model(df: pd.DataFrame, model_path: str = "models/loan_model.pkl") -> None:
    try:
        # Encode categorical features
        df_encoded = df.copy()
        label_encoders = {}
        for column in df_encoded.select_dtypes(include='object').columns:
            if column != 'Loan_Approved':
                le = LabelEncoder()
                df_encoded[column] = le.fit_transform(df_encoded[column])
                label_encoders[column] = le
        
        # Encode target variable
        target_encoder = LabelEncoder()
        df_encoded['Loan_Approved'] = target_encoder.fit_transform(df_encoded['Loan_Approved'])

        X = df_encoded.drop('Loan_Approved', axis=1)
        y = df_encoded['Loan_Approved']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        with open(model_path, 'wb') as f:
            pickle.dump((model, label_encoders, target_encoder), f)

        logging.info("Model trained and saved to %s", model_path)

    except Exception as e:
        logging.error("Error training model: %s", e)
        raise
