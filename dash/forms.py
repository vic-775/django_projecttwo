from django import forms
from .models import approvals

class DataForm(forms.ModelForm):
    class Meta:
        model = approvals
        fields = ['name','dependants','applicants_income','coapplicants_income','loan_amount',
                    'loan_term','credit_history','gender','marital_status','education_status',
                    'self_employed','area','loan_status']