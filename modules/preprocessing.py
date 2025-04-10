# modules/preprocessing.py

import pandas as pd
import logging

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    try:
        # Convert data types
        df['Credit_History'] = df['Credit_History'].astype('object')
        df['Loan_Amount_Term'] = df['Loan_Amount_Term'].astype('object')

        # Fill missing categorical values
        df['Gender'].fillna('Male', inplace=True)
        df['Married'].fillna(df['Married'].mode()[0], inplace=True)
        df['Dependents'].fillna(df['Dependents'].mode()[0], inplace=True)
        df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace=True)
        df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace=True)
        df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace=True)

        # Fill missing numerical values
        df['LoanAmount'].fillna(df['LoanAmount'].median(), inplace=True)

        # Drop Loan_ID if exists
        if 'Loan_ID' in df.columns:
            df.drop('Loan_ID', axis=1, inplace=True)

        logging.info("Data cleaned successfully.")
        return df

    except Exception as e:
        logging.error("Error in cleaning data: %s", e)
        raise
