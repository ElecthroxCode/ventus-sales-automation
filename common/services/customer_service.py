from apps.customers.models import Customer
from django.db.models import Q

def create_customer(data):
    nit = data.get("nit")
    if not nit:
        raise ValueError("NIT es requerido")

    customer = Customer.objects.filter(nit=nit).first()
    if customer:
        return customer, True  # existe

    required_fields = ['name', 'lastname', 'email', 'phone']
    for field in required_fields:
        if not data.get(field):
            raise ValueError(f"{field} es requerido")

    if Customer.objects.filter(email=data.get('email')).exists():
        raise ValueError("El email ya está registrado")

    customer = Customer.objects.create(
        name=data.get('name'),
        lastname=data.get('lastname'),
        email=data.get('email'),
        phone=data.get('phone'),
        nit=nit
    )
    return customer, False


def list_customers(search=None):
    """Listar clientes con filtro opcional por nombre, apellido o NIT"""
    customers = Customer.objects.all()
    if search:
        customers = customers.filter(
            Q(name__icontains=search) |
            Q(lastname__icontains=search) |
            Q(nit__icontains=search)
        )
    return customers


def get_customer_detail(pk):
    """Obtener detalle de un cliente por ID"""
    try:
        return Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return None