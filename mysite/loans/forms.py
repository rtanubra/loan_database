from django import forms
from .models import Loan

class LoanAddForm(forms.ModelForm):
    
    class Meta:
        model = Loan
        fields = [
            'loan_name',
            'loan_start_date',
            'loan_starting_principal',
            'loan_principal',
            'loan_last_action_date',
            'loan_interest',
            'loan_payment'
        ]

class LoanEmailForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

