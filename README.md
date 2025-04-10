# Loan Eligibility Prediction App

This is a machine learning project that predicts loan approval based on applicant information. The application is built using Python and deployed with Streamlit to provide an interactive web interface.

## Project Author

- **Name**: Vasanth Gnana Seelan  
- **GitHub**: [https://github.com/vasanthgnanaseelan](https://github.com/vasanthgnanaseelan)

## Project Description

The model takes in user input such as income, credit history, education, and employment status, and predicts whether a loan application is likely to be approved. The model was trained on a real-world dataset using a Random Forest Classifier.

## Features

- User-friendly web interface built with Streamlit
- Model training and saving using Scikit-learn
- Input validation and logging
- Modular code for easy maintenance and reuse

## Folder Structure

```
loan_eligibility_project/
├── app/
│   └── app.py                  # Streamlit application
├── modules/
│   ├── data_loader.py          # Data loading logic
│   ├── preprocessing.py        # Data cleaning and preprocessing
│   ├── model.py                # Model training and saving
│   ├── predict.py              # Model loading and predictions
│   └── utils.py                # Logging setup
├── data/
│   └── credit.csv              # Source dataset
├── models/
│   └── loan_model.pkl          # Trained model file
├── logs/
│   └── app.log                 # Application logs
├── train.py                    # Script to train and save the model
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Files to exclude from version control
```

## How to Run the Project

1. Clone the repository:
   ```
   git clone https://github.com/vasanthgnanaseelan/loan-eligibility-project.git
   cd loan-eligibility-project
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Train the model:
   ```
   python train.py
   ```

4. Launch the Streamlit app:
   ```
   streamlit run app/app.py
   ```

## Deployment

The app is ready to be deployed on Streamlit Cloud. Just push your repository to GitHub and connect it to your Streamlit account at https://streamlit.io/cloud.

Already deployed : https://vasanthgnanaseelan-loan-eligibility-model-solutio-appapp-yxd8st.streamlit.app/

## License

This project is provided for educational purposes only.

