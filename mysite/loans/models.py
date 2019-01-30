from django.db import models
import datetime

# Create your models here.
class Loan(models.Model):
    def __str__(self):
        return self.loan_name
    loan_name = models.CharField(max_length=100,unique=True)
    loan_start_date = models.DateField(default=datetime.date.today())
    loan_starting_principal = models.DecimalField(max_digits=9,decimal_places=2)
    loan_principal = models.DecimalField(max_digits=9,decimal_places=2)
    loan_interest = models.DecimalField(max_digits =5, decimal_places=4) 
    loan_amort_months = models.IntegerField()