from django.urls import path
from .views import (
    LoanListView,
    #LoanDetailView,
    #LoanCreateView,
)

app_name="loans"
urlpatterns = [
    path("",LoanListView.as_view(),name="article_list")
]