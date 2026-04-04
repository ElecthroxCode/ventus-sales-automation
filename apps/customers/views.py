from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from apps.customers.models import Customer


# 🔹 CREAR CLIENTE
class CustomerCreateView(APIView):

    def post(self, request):

        nit = request.data.get('nit')

        if not nit:
            return Response(
                {"error": "NIT es requerido"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 🔍 BUSCAR SI YA EXISTE
        customer = Customer.objects.filter(nit=nit).first()

        if customer:
            return Response({
                "id": customer.id,
                "name": customer.name,
                "lastname": customer.lastname,
                "email": customer.email,
                "phone": customer.phone,
                "nit": customer.nit,
                "exists": True
            }, status=status.HTTP_200_OK)

        # 🔥 VALIDACIONES
        required_fields = ['name', 'lastname', 'email', 'phone']

        for field in required_fields:
            if not request.data.get(field):
                return Response(
                    {"error": f"{field} es requerido"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # 🔥 VALIDAR EMAIL ÚNICO
        if Customer.objects.filter(email=request.data.get('email')).exists():
            return Response(
                {"error": "El email ya está registrado"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 🔹 CREAR
        try:
            customer = Customer.objects.create(
                name=request.data.get('name'),
                lastname=request.data.get('lastname'),
                email=request.data.get('email'),
                phone=request.data.get('phone'),
                nit=nit
            )

            return Response({
                "id": customer.id,
                "name": customer.name,
                "lastname": customer.lastname,
                "email": customer.email,
                "phone": customer.phone,
                "nit": customer.nit,
                "exists": False
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


# 🔥 🔥 NUEVO: LISTAR + BUSCAR (LO QUE TE FALTABA)
class CustomerListView(APIView):

    def get(self, request):

        search = request.GET.get('search')

        customers = Customer.objects.all()

        # 🔍 BUSQUEDA PRO
        if search:
            customers = customers.filter(
                Q(name__icontains=search) |
                Q(lastname__icontains=search) |
                Q(nit__icontains=search)
            )

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


# 🔹 BUSCAR SOLO POR NIT
class CustomerSearchView(APIView):

    def get(self, request):

        nit = request.GET.get('nit')

        if not nit:
            return Response({}, status=status.HTTP_200_OK)

        customer = Customer.objects.filter(nit=nit).first()

        if customer:
            return Response({
                "id": customer.id,
                "name": customer.name,
                "lastname": customer.lastname,
                "email": customer.email,
                "phone": customer.phone,
                "nit": customer.nit
            })

        return Response({})


# 🔹 DETALLE
class CustomerDetailView(APIView):

    def get(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)

            return Response({
                "id": customer.id,
                "name": customer.name,
                "lastname": customer.lastname,
                "email": customer.email,
                "phone": customer.phone,
                "nit": customer.nit
            })

        except Customer.DoesNotExist:
            return Response(
                {"error": "Cliente no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )