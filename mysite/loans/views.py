from django.shortcuts import render,redirect,get_object_or_404

from .models import Loan

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    View
)

# Create your views here.
class LoanListView(ListView):
    template_name = "loan/loan_list.html"
    queryset = Loan.objects.all()