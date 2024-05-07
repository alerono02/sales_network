from django.urls import include, path
from rest_framework.routers import DefaultRouter
from suppliers.views import SupplierViewSet
from suppliers.apps import SupplierConfig as cfg

app_name = cfg.name

suppliers_router = DefaultRouter()
suppliers_router.register(r'suppliers', SupplierViewSet, basename='suppliers')

urlpatterns = [
    path('', include(suppliers_router.urls)),
]