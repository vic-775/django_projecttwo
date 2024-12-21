from django.db import models
import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Define constants for categorical fields (these can be global if needed)
GENDER = (
    (0, 'Female'),
    (1, 'Male')
)

MARITAL_STATUS = (
    (1, 'Yes'),
    (0, 'No')
)

EDUCATION = (
    (0, 'Graduated'),
    (1, 'Non_Graduate')
)

SELF_EMPLOYED = (
    (1, 'Yes'),
    (0, 'No')
)

AREA = (
    (0, 'Rural'),
    (1, 'Semi-Urban'),
    (2, 'Urban')
)

class approvals(models.Model):
    # Define fields (no changes here)
    name = models.CharField(max_length=100, null=True)
    dependants = models.PositiveBigIntegerField(null=True)
    applicants_income = models.PositiveBigIntegerField(null=True)
    coapplicants_income = models.PositiveBigIntegerField(null=True)
    loan_amount = models.PositiveBigIntegerField(null=True)
    loan_term = models.PositiveBigIntegerField(null=True)
    credit_history = models.IntegerField(null=True)
    gender = models.IntegerField(choices=GENDER, null=True)
    marital_status = models.IntegerField(choices=MARITAL_STATUS, null=True)
    education_status = models.IntegerField(choices=EDUCATION, null=True)
    self_employed = models.IntegerField(choices=SELF_EMPLOYED, null=True)
    area = models.IntegerField(choices=AREA, null=True)
    loan_status = models.CharField(max_length=10, blank=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def save(self, *args, **kwargs):
    # Load the machine learning model
        ml_model = joblib.load('ml_model/loan_nn_model4.pkl')

    # Construct input_data in the correct order
        input_data = np.array([[
        self.gender,             
        self.marital_status,     
        self.dependants,         
        self.education_status,   
        self.self_employed,      # Self_Employe
        self.applicants_income,  # ApplicantIncome
        self.coapplicants_income, # CoapplicantIncome
        self.loan_amount,        # LoanAmount
        self.loan_term,          # Loan_Amount_Term
        self.credit_history,     # Credit_History
        self.area]])

    # Predict loan status
        self.loan_status = ml_model.predict(input_data)[0]

    # Save the instance
        super().save(*args, **kwargs)

