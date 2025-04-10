# modules/data_loader.py

import pandas as pd
import logging

def load_data(path=r'E:\BISI\Machine learning\Project\Loan_Eligibility_Model_Solution\data\credit.csv'):
    try:
        df = pd.read_csv(path)
        logging.info("Data loaded successfully from %s", path)
        return df
    except Exception as e:
        logging.error("Failed to load data: %s", e)
        raise
