from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from apps.sales.models import Sale
# Create your views here.


class SalesReportView(APIView):

    def get(self, request):
        sales = Sale.objects.all()

        customer_id = request.query_params.get('customer')
        if customer_id:
            sales = sales.filter(customer_id=customer_id)

        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if start_date:
            sales = sales.filter(date__gte=start_date)

        if end_date:
            sales = sales.filter(date__lte=end_date)

        total = sales.aggregate(total_income=Sum('total'))
        total["total_income"] = total["total_income"] or 0

        return Response(total)
    


