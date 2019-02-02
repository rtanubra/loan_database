from django.urls import path
from .views import (
    PaymentCreateView,
    PaymentListView,
)

app_name="payments"
urlpatterns = [
    path("<int:loan_id>/create/",PaymentCreateView.as_view(),name="payment_create"),
    path("<int:loan_id>/list/",PaymentListView.as_view(),name='payment_list')
]