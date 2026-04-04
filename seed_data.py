from apps.sales.models import Sale, SaleDetail
from apps.customers.models import Customer
from apps.products.models import Product
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

print("🚀 Iniciando carga de datos...")

customers = list(Customer.objects.all())
products = list(Product.objects.all())
user = User.objects.first()

if len(customers) < 2 or len(products) < 4:
    print("❌ Necesitas al menos 2 clientes y 4 productos")
    exit()

# =========================
# 🔥 VENTA 1 (HOY)
# =========================
sale1 = Sale.objects.create(
    customer=customers[0],
    user=user,
    payment_method='cash',
    date=timezone.now(),
    total=0
)

p1 = products[0]

SaleDetail.objects.create(
    sale=sale1,
    product=p1,
    quantity=2,
    unit_price=p1.price,
    subtotal=p1.price * 2
)

sale1.total = p1.price * 2
sale1.save()

# =========================
# 🔥 VENTA 2 (AYER)
# =========================
sale2 = Sale.objects.create(
    customer=customers[1],
    user=user,
    payment_method='card',
    date=timezone.now() - timedelta(days=1),
    total=0
)

p2 = products[1]

SaleDetail.objects.create(
    sale=sale2,
    product=p2,
    quantity=1,
    unit_price=p2.price,
    subtotal=p2.price
)

sale2.total = p2.price
sale2.save()

# =========================
# 🔥 VENTA 3 (HACE 3 DÍAS)
# =========================
sale3 = Sale.objects.create(
    customer=customers[0],
    user=user,
    payment_method='transfer',
    date=timezone.now() - timedelta(days=3),
    total=0
)

p3 = products[2]

SaleDetail.objects.create(
    sale=sale3,
    product=p3,
    quantity=3,
    unit_price=p3.price,
    subtotal=p3.price * 3
)

sale3.total = p3.price * 3
sale3.save()

# =========================
# 🔥 VENTA 4 (HACE 7 DÍAS)
# =========================
sale4 = Sale.objects.create(
    customer=customers[1],
    user=user,
    payment_method='cash',
    date=timezone.now() - timedelta(days=7),
    total=0
)

p4 = products[3]

SaleDetail.objects.create(
    sale=sale4,
    product=p4,
    quantity=2,
    unit_price=p4.price,
    subtotal=p4.price * 2
)

sale4.total = p4.price * 2
sale4.save()

print("🔥 Datos de prueba creados correctamente")