from django import forms
import datetime
from .models import Payment
from django.forms.widgets import HiddenInput

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'payment_loan',
            'payment_amount',
            'payment_date'
        ]

    def __init__(self,*args,**kwargs):
        hide_condition= kwargs.pop('hide_condition',None)
        super(PaymentForm,self).__init__(*args,**kwargs)
        if hide_condition:
            self.fields["payment_loan"].widget=HiddenInput()
