from ..models.insurance import Insurance
from ..serializers.insurance import InsuranceSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from ..pagination import PostPageNumberPagination


class InsuranceViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['car__make', 'insurance_company', 'type_of_insurance']
    ordering_fields = ['insurance_company', 'end_date', 'type_of_insurance', 'worth_of_insurance']
    pagination_class = PostPageNumberPagination

    def perform_create(self, serializer):

        """Change of insurance status."""

        if serializer.validated_data['insurance_status'] == True:
            car_id = serializer.validated_data['car']
            Insurance.objects.filter(car=car_id, insurance_status=True).update(insurance_status=False)
        serializer.save()
