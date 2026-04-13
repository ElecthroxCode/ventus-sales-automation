import random
from datetime import timedelta
from django.utils import timezone

from apps.sales.models import Sale, SaleDetail
from apps.customers.models import Customer
from apps.products.models import Product, Category
from django.contrib.auth.models import User

print("🚀 Iniciando carga de datos...")

# =========================
# 👤 USER
# =========================
user = User.objects.first()

# =========================
# 🧑 CLIENTES
# =========================
if Customer.objects.count() == 0:
    customers = [
        Customer.objects.create(name="Juan Perez", email="juan@test.com"),
        Customer.objects.create(name="Maria Gomez", email="maria@test.com"),
        Customer.objects.create(name="Carlos Lopez", email="carlos@test.com"),
    ]
else:
    customers = list(Customer.objects.all())

# =========================
# 📦 CATEGORIAS
# =========================
if Category.objects.count() == 0:
    cat1 = Category.objects.create(name="Tecnología")
    cat2 = Category.objects.create(name="Accesorios")
else:
    cat1, cat2 = Category.objects.all()[:2]

# =========================
# 🛒 PRODUCTOS
# =========================
if Product.objects.count() == 0:
    products = [
        Product.objects.create(name="Laptop", price=2500, category=cat1),
        Product.objects.create(name="Teclado", price=150, category=cat2),
        Product.objects.create(name="Mouse", price=80, category=cat2),
        Product.objects.create(name="Monitor", price=900, category=cat1),
        Product.objects.create(name="Audífonos", price=200, category=cat2),
    ]
else:
    products = list(Product.objects.all())

# =========================
# 🔥 FUNCIÓN PARA CREAR VENTAS
# =========================
def create_sales(quantity, days_ago):
    for _ in range(quantity):
        customer = random.choice(customers)
        product = random.choice(products)
        qty = random.randint(1, 3)

        date = timezone.now() - timedelta(days=days_ago)

        sale = Sale.objects.create(
            customer=customer,
            user=user,
            payment_method=random.choice(['cash', 'card', 'transfer']),
            date=date,
            total=0
        )

        subtotal = product.price * qty

        SaleDetail.objects.create(
            sale=sale,
            product=product,
            quantity=qty,
            unit_price=product.price,
            subtotal=subtotal
        )

        sale.total = subtotal
        sale.save()

# =========================
#  DISTRIBUCIÓN DE VENTAS
# =========================

create_sales(10, 30)  # hace 30 días
create_sales(7, 15)   # hace 15 días
create_sales(10, 7)   # hace 7 días
create_sales(5, 0)    # hoy

print("Datos creados correctamente")