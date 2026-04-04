from apps.sales.models import Sale, SaleDetail
from apps.customers.models import Customer
from django.contrib.auth.models import User
from apps.products.models import Product
from django.db import transaction
from decimal import Decimal


@transaction.atomic
def create_sale(data):

    # 🔥 VALIDACIÓN BÁSICA
    if not data.get("products"):
        raise ValueError("La venta debe tener al menos un producto")

    # 🔹 Obtener cliente y usuario
    try:
        customer = Customer.objects.get(id=data["customer_id"])
    except Customer.DoesNotExist:
        raise ValueError("Cliente no existe")

    try:
        user = User.objects.get(id=data["user_id"])
    except User.DoesNotExist:
        raise ValueError("Usuario no existe")

    # 🔹 Crear venta inicial
    sale = Sale.objects.create(
        customer=customer,
        user=user,
        payment_method=data["payment_method"],
        total=Decimal('0.00')
    )

    total = Decimal('0.00')

    # 🔹 Procesar productos
    for item in data["products"]:
        product_id = item.get("product_id")
        quantity = int(item.get("quantity", 0))

        if quantity <= 0:
            raise ValueError("Cantidad inválida")

        # 🔥 BLOQUEO DE FILA
        try:
            product = Product.objects.select_for_update().get(id=product_id)
        except Product.DoesNotExist:
            raise ValueError(f"Producto {product_id} no existe")

        # 🔥 VALIDAR STOCK
        if product.stock_quantity < quantity:
            raise ValueError(
                f"Stock insuficiente para {product.name}. Disponible: {product.stock_quantity}"
            )

        unit_price = product.price
        subtotal = unit_price * quantity

        # 🔹 Crear detalle
        SaleDetail.objects.create(
            sale=sale,
            product=product,
            quantity=quantity,
            unit_price=unit_price,
            subtotal=subtotal
        )

        # 🔥 DESCONTAR STOCK (optimizado)
        product.stock_quantity -= quantity
        product.save(update_fields=["stock_quantity"])

        total += subtotal

    # 🔹 Guardar total final
    sale.total = total
    sale.save(update_fields=["total"])

    return sale