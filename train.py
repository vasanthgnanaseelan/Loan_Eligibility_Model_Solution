# train.py

from modules.data_loader import load_data
from modules.preprocessing import clean_data
from modules.model import train_model
from modules.utils import setup_logging

setup_logging()
df = load_data(path=r'E:\BISI\Machine learning\Project\Loan_Eligibility_Model_Solution\data\credit.csv')  # <- FIXED path
df_cleaned = clean_data(df)
train_model(df_cleaned)
