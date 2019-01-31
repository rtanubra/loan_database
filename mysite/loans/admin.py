from django.contrib import admin

# Register your models here.
from .models import Loan
from payments.models import Payment

admin.site.register(Loan)
admin.site.register(Payment)