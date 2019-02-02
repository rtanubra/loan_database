from django.contrib import admin

# Register your models here.
from .models import Loan
from payments.models import Payment
from payments.models import PaymentTracker

admin.site.register(Loan)
admin.site.register(Payment)
admin.site.register(PaymentTracker)