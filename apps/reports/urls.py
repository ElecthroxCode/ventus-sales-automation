from django.urls import path
from .views import SalesReportView

urlpatterns = [
    path('sales/total/', SalesReportView.as_view(), name='sales-total'),
]
