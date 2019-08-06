from ..models.car import Car
from ..serializers.car import CarSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from ..pagination import PostPageNumberPagination


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['status', 'make', 'model', 'fuel_types', 'transmission', 'color']
    ordering_fields = ['make', 'model', 'price_per_day', 'engine', 'year_of_manufacture']
    pagination_class = PostPageNumberPagination
