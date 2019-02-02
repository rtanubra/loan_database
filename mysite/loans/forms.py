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
"""
loan_name = models.CharField(max_length=100,unique=True)
loan_start_date = models.DateField(default=datetime.date.today())
loan_starting_principal = models.DecimalField(max_digits=9,decimal_places=2)
loan_principal = models.DecimalField(max_digits=9,decimal_places=2)
loan_last_action_date = models.DateField(default=datetime.date.today())
loan_interest = models.DecimalField(max_digits =5, decimal_places=4) 
loan_payment = models.DecimalField(max_digits=6,decimal_places=2,default=350)
"""