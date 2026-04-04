from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from apps.sales.serializers.sale_serializer import SaleCreateSerializer
from common.services.sale_service import create_sale

from apps.sales.models import Sale
from apps.sales.serializers.sale_list_serializer import SaleListSerializer


class SaleCreateView(APIView):

    def post(self, request):
        serializer = SaleCreateSerializer(data=request.data)

        if serializer.is_valid():
            try:
                sale = create_sale(serializer.validated_data)

                return Response({
                    "message": "Venta creada correctamente",
                    "sale_id": sale.id
                }, status=status.HTTP_201_CREATED)

            except ValueError as e:
                return Response({
                    "error": str(e)
                }, status=status.HTTP_400_BAD_REQUEST)

            except Exception as e:
                return Response({
                    "error": "Error interno del servidor"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesListView(APIView):

    def get(self, request):
        sales = Sale.objects.select_related('customer')

        # 🔥 BUSQUEDA PRO (nombre, apellido, NIT)
        search = request.query_params.get('search')
        if search:
            sales = sales.filter(
                Q(customer__name__icontains=search) |
                Q(customer__lastname__icontains=search) |
                Q(customer__nit__icontains=search)
            )

        # 🔹 método de pago
        payment_method = request.query_params.get('payment_method')
        if payment_method:
            sales = sales.filter(payment_method=payment_method)

        # 🔹 fechas
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        if start_date and end_date:
            sales = sales.filter(date__date__range=[start_date, end_date])

        serializer = SaleListSerializer(sales, many=True)
        return Response(serializer.data)


class PaymentMethodListView(APIView):

    def get(self, request):
        return Response([
            {"value": "cash", "label": "Efectivo"},
            {"value": "card", "label": "Tarjeta"},
            {"value": "transfer", "label": "Transferencia"},
        ])


class SaleDetailView(APIView):

    def get(self, request, pk):
        try:
            sale = Sale.objects.prefetch_related('details').get(pk=pk)
        except Sale.DoesNotExist:
            return Response({"error": "Venta no encontrada"}, status=404)

        serializer = SaleListSerializer(sale)
        return Response(serializer.data)