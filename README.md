# 🛒 Ventus Project – Sistema Inteligente de Ventas

## 📌 Descripción
Aplicación web desarrollada con **Django + Django REST Framework** para la gestión de ventas, clientes y productos.  
El sistema integra un **dashboard interactivo** y una **API REST desacoplada**, aplicando arquitectura limpia y separación de responsabilidades.

## 🚀 Funcionalidades principales
- Registro y gestión de clientes 👥  
- Catálogo de productos con control de stock 📦  
- Registro de ventas con detalle de productos 💳  
- Descuento automático de inventario 🔄  
- Dashboard con métricas y gráficas 📊  
- Filtros avanzados en ventas (cliente, fecha, método de pago) 🔍  
- Reportes y KPIs (en roadmap) 📈  

## 🏗️ Arquitectura
El proyecto sigue una arquitectura en capas desacopladas:

```
Frontend (HTML + JS)
↓
Dashboard (Vistas HTML)
↓
API REST (Django Rest Framework)
↓
Services (Lógica de negocio)
↓
Models (Base de datos)
```

📌 **Frase clave:**  
**El dashboard muestra, la API responde, el service decide.**

### 📂 Estructura de carpetas
```
app/
 ├── customer/
 │    ├── models.py
 │    ├── urls.py
 │    └── views.py
 │
 ├── dashboard/
 │    ├── static/dashboard/
 │    │     ├── vendors/
 │    │     └── images/
 │    ├── template/dashboard/
 │    │     ├── base_site.html
 │    │     ├── create_product.html
 │    │     ├── create_sales.html
 │    │     ├── customer_detail.html
 │    │     ├── customers_list.html
 │    │     ├── index.html
 │    │     ├── products_list.html
 │    │     ├── sales_detail.html
 │    │     ├── sales_list.html
 │    │     └── sidebar.html
 │    ├── views/dashboard_views.py
 │    └── urls.py
 │
 ├── products/
 │    ├── serializers/products_serializer.py
 │    ├── models.py
 │    ├── urls.py
 │    └── views.py
 │
 ├── sales/
 │    ├── serializers/
 │    │     ├── sale_list_serializer.py
 │    │     └── sale_serializer.py
 │    ├── models.py
 │    ├── urls.py
 │    └── views.py
 │
 ├── users/
 │    ├── models.py
 │    └── views.py
 │
 └── reports/   (pendiente de implementación)

common/
 └── services/
      └── sale_service.py

config/
 ├── exception/
 ├── permissions/
 ├── services/
 ├── setting/
 │    ├── base.py
 │    ├── local.py
 │    └── production.py
 └── urls.py
```

## 📊 Modelo Entidad-Relación (MER)
![Diagrama MER](docs/images/mer-diagram.jpg)

## 🔗 Endpoints principales
- `GET /api/customers/` → Listado de clientes  
- `GET /api/customers/<id>/` → Detalle de cliente  
- `GET /api/products/` → Listado de productos  
- `POST /api/sales/create/` → Crear venta  
- `GET /api/sales/` → Listado de ventas  
- `GET /api/sales/<id>/` → Detalle de venta  

## ⚙️ Tecnologías utilizadas
- **Backend:** Python, Django, Django REST Framework  
- **Frontend:** HTML, JavaScript, Chart.js  
- **Arquitectura:** Services, Serializers, Views, Models  
- **Base de datos:** PostgreSQL (recomendado)  

## 📈 Flujo de una venta
1. El usuario selecciona productos en el dashboard.  
2. El frontend envía `customer_id` y `products[]` vía API.  
3. `create_sale()` valida stock y descuenta inventario.  
4. Se crea la venta y sus detalles en la base de datos.  
5. El dashboard muestra la confirmación y métricas actualizadas.  

## ✅ Buenas prácticas aplicadas
- Separación de responsabilidades  
- API desacoplada del dashboard  
- Lógica de negocio en services reutilizables  
- Validación con serializers  
- Frontend independiente consumiendo API  

## 🔮 Mejoras futuras
- Historial de compras por cliente  
- Reportes avanzados y KPIs  
- Paginación en listados  
- Mejor UX (loading, alerts, feedback)  
- Dashboard más interactivo
