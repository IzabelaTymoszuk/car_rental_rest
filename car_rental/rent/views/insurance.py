from ..models.insurance import Insurance
from ..serializers.insurance import InsuranceSerializer
from rest_framework import viewsets
from rest_framework import permissions


class InsuranceViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
