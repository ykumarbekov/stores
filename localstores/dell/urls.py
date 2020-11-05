from django.urls import path
from . import views

urlpatterns = [
    path('customers', views.customers, name='customers'),
    ]

# Examples:
# customers?ordering=date&start=10.09.2004&end=25.09.2004
# customers?country=country
