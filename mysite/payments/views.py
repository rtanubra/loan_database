from django.shortcuts import render,redirect,get_object_or_404

from .models import Payment, PaymentTracker
from loans.models import Loan
from .forms import PaymentForm
# Create your views here.
from datetime import datetime, timedelta, date
from django.urls import reverse
from django.views.generic import (
    TemplateView,
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    View
)
class PaymentObjectMixin(object):

    def get_object(self,lookup,model):
        id = lookup
        model = model
        if id is not None:
            obj = get_object_or_404(model,id=id)

class PaymentListView(TemplateView):
    template_name = "payments/payment_list.html"
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        loan_id = self.kwargs.get("loan_id")
        loan = get_object_or_404(Loan,id=loan_id)
        context["loan"] = loan
        context["object_list"] = PaymentTracker.objects.filter(payment_loan=loan)
        
        return context


    

class PaymentCreateView(PaymentObjectMixin,View):

    def __init__(self):
        self.template_name= "payments/payment_create.html"

    def get(self,request,*args,**kwargs):
        loan_id = self.kwargs.get("loan_id")
        loan = get_object_or_404(Loan,id=loan_id)
        initial_data = {
            'payment_loan' : loan
        }
        form = PaymentForm(request.POST or None,initial=initial_data,hide_condition=True)
        context = {
            'form':form,
            'loan' : loan
        }
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form = PaymentForm(request.POST)
        if form.is_valid():
            new_payment = form.save()
            #=======Necessary variables for calc =====#
            loan = get_object_or_404(Loan,id= new_payment.payment_loan.id) 
            days_diff = (new_payment.payment_date - loan.loan_last_action_date).days
            pmt = new_payment.payment_amount
            interest_paid = round(days_diff*loan.loan_interest/365*loan.loan_principal,2)
            interest_per_day = round(loan.loan_interest/365*loan.loan_principal,2)
            principal_paid = round(pmt-interest_paid,2)
            principal_pre =round(loan.loan_principal,2)
            new_principal = round(principal_pre-principal_paid,2)
            current_loan_interest = round(loan.loan_interest,2)
            new_loan_interest = round(current_loan_interest + interest_paid,2)
            #=======PaymentTracker=============#
            PaymentTracker.objects.create(
                payment_loan = loan,
                payment_pre_principal = loan.loan_principal,
                payment_amount = new_payment.payment_amount,
                payment_ipd = interest_per_day,
                payment_interest_paid = interest_paid,
                payment_principal_paid = principal_paid,
                payment_post_principal = loan.loan_principal - principal_paid,
                payment_date = new_payment.payment_date
            )
            #==========Update Loan=============#
            #Theory cannot have operations while updating directly to database
            #if we did it through update wrapper perhaps that would be more pythonic
            loan.loan_principal = round(new_principal,2)
            loan.loan_last_action_date = new_payment.payment_date
            loan.save()
            loan_id = self.kwargs.get("loan_id")
            loan = get_object_or_404(Loan,id=loan_id)
            initial_data = {
            'payment_loan' : loan
            }
            form = PaymentForm(initial=initial_data,hide_condition=True)
            context = {
                'form':form,
                'loan' : loan
            }
            return render(request,self.template_name,context)


    
