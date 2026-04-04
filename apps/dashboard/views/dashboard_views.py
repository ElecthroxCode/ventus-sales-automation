from django.shortcuts import render
from apps.sales.models import Sale, SaleDetail
from apps.customers.models import Customer
from django.db.models import Sum, Avg
from django.utils.timezone import now
from datetime import timedelta
from django.db.models.functions import TruncDate
from datetime import datetime
from apps.products.models import Product

import json


def dashboard_home(request):

    # 🔥 FILTRO POR FECHA
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    sales = Sale.objects.all()

    if start_date and end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        sales = sales.filter(date__range=[start_date, end_date])

    # 🔹 KPIs
    total_sales = sales.count()
    total_customers = Customer.objects.count()

    total_revenue = sales.aggregate(
        total=Sum('total')
    )['total'] or 0

    avg_ticket = sales.aggregate(
        avg=Avg('total')
    )['avg'] or 0

    # 🔹 PRODUCTOS VENDIDOS (IMPORTANTE: usar sales filtradas)
    total_products_sold = (
        SaleDetail.objects
        .filter(sale__in=sales)
        .aggregate(total=Sum('quantity'))
    )['total'] or 0

    # 🔹 VENTAS DEL DÍA (esto lo puedes dejar global o filtrar también)
    today_sales = Sale.objects.filter(
        date__date=now().date()
    ).count()

    # 🔹 NUEVOS CLIENTES
    new_customers = Customer.objects.filter(
        created_at__gte=now() - timedelta(days=7)
    ).count()

    # 🔹 GRÁFICO DE LÍNEA
    sales_by_day = (
        sales
        .annotate(day=TruncDate('date'))
        .values('day')
        .annotate(total=Sum('total'))
        .order_by('day')
    )

    sales_labels = [str(item['day']) for item in sales_by_day]
    sales_data = [float(item['total']) for item in sales_by_day]

    # 🔹 TOP PRODUCTOS (FILTRADO)
    top_products = (
        SaleDetail.objects
        .filter(sale__in=sales)
        .values('product__name')
        .annotate(total_sold=Sum('quantity'))
        .order_by('-total_sold')[:5]
    )

    bar_labels = [item['product__name'] for item in top_products]
    bar_data = [item['total_sold'] for item in top_products]

    # 🔹 PIE POR CATEGORÍA (FILTRADO)
    sales_by_category = (
        SaleDetail.objects
        .filter(sale__in=sales)
        .values('product__category__name')
        .annotate(total=Sum('quantity'))
    )

    pie_labels = [item['product__category__name'] for item in sales_by_category]
    pie_data = [item['total'] or 0 for item in sales_by_category]

    # botones del filtro
    today = now().date()
    last_7_days = today - timedelta(days=7)

    context = {
        'total_sales': total_sales,
        'total_customers': total_customers,
        'total_revenue': total_revenue,
        'total_products_sold': total_products_sold,
        'today_sales': today_sales,
        'new_customers': new_customers,
        'avg_ticket': avg_ticket,
        'today': today,
        'last_7_days': last_7_days,

        'sales_labels': json.dumps(sales_labels),
        'sales_data': json.dumps(sales_data),

        'bar_labels': json.dumps(bar_labels),
        'bar_data': json.dumps(bar_data),

        'pie_labels': json.dumps(pie_labels),
        'pie_data': json.dumps(pie_data),
    }

    return render(request, 'dashboard/index.html', context)

#Vista - formulario create-sales
def create_sale(request):
    customers = Customer.objects.all()
    products = Product.objects.all()

    context = {
        'customers': customers,
        'products': products
    }

    return render(request, 'dashboard/create_sales.html', context)



#vista-lista de ventas
def sales_list(request):
    return render(request, 'dashboard/sales_list.html')


#vista-lista de productos
def products_list(request):
    return render(request, 'dashboard/products_list.html')

#vista detalles de venta
def sales_detail_view(request, pk):
    return render(request, "dashboard/sales_detail.html")

#vista customers
def customers_view(request):
    return render(request, "dashboard/customers_list.html")


# 🔹 vista detalle de cliente
def customer_detail_view(request, pk):
    return render(request, "dashboard/customer_detail.html", {
        "customer_id": pk
    })