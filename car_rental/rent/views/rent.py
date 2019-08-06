from ..models.rent import Rent
from ..serializers.rent import RentSerializer
from rest_framework import viewsets
from rest_framework import permissions


class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]