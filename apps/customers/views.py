from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common.services.customer_service import create_customer, list_customers, get_customer_detail

class CustomerCreateView(APIView):
    def post(self, request):
        try:
            customer, exists = create_customer(request.data)
            return Response({
                "id": customer.id,
                "name": customer.name,
                "lastname": customer.lastname,
                "email": customer.email,
                "phone": customer.phone,
                "nit": customer.nit,
                "exists": exists
            }, status=status.HTTP_200_OK if exists else status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CustomerListView(APIView):
    def get(self, request):
        search = request.GET.get('search')
        customers = list_customers(search)
        data = [
            {
                "id": c.id,
                "name": c.name,
                "lastname": c.lastname,
                "email": c.email,
                "phone": c.phone,
                "nit": c.nit
            }
            for c in customers
        ]
        return Response(data)


class CustomerDetailView(APIView):
    def get(self, request, pk):
        customer = get_customer_detail(pk)
        if customer:
            return Response({
                "id": customer.id,
                "name": customer.name,
                "lastname": customer.lastname,
                "email": customer.email,
                "phone": customer.phone,
                "nit": customer.nit
            })
        return Response({"error": "Cliente no encontrado"}, status=status.HTTP_404_NOT_FOUND)