from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from apps.products.models import Product
from apps.products.serializers.products_serializer import ProductSerializer

# Create your views here.

class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        #buscador
        search = request.query_params.get('search')
        #buscar por producto o categoria
        if search:
            products = products.filter(
                Q(name__icontains=search) |
                Q(category__name__icontains=search)
            )

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)