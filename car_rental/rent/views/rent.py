from ..models.rent import Rent
from ..serializers.rent import RentSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from ..pagination import PostPageNumberPagination


class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['car']
    ordering_fields = ['start_rent', 'end_rent', 'deposit', 'number_of_day', 'amount', 'car']
    pagination_class = PostPageNumberPagination

    def perform_create(self, serializer):

        """Change of car status."""

        car = serializer.validated_data['car']
        if car.status == 'A':
            car.status = 'R'
            car.save()
        serializer.save()
