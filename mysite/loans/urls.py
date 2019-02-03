from django.urls import path
from .views import (
    LoanListView,
    #LoanDetailView,
    LoanCreateView,
    LoanEmailView,
)

app_name="loans"
urlpatterns = [
    path("",LoanListView.as_view(),name="loan_list"),
    path("create/",LoanCreateView.as_view(),name="loan_create"),
    path("send/",LoanEmailView.as_view(),name='loan_email')
]