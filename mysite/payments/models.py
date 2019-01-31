from django.db import models
from datetime import date
from loans.models import Loan
# Create your models here.

class Payment(models.Model):
    def __str__(self):
        return f"Payment {self.payment_loan.loan_name} - {self.payment_date}"
    payment_loan = models.ForeignKey(Loan,on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=7, decimal_places=2)
    payment_date = models.DateField(default=date.today())