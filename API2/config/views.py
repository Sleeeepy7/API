from datetime import datetime
import django_filters.rest_framework
from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from config.models import Service
from config.serializers import ServiceSerializer



class ServiceApi(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['from_date', 'to_date', 'views', 'clicks', 'cost']  # фильтрация по всем полям



# class ServiceList(generics.ListCreateAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#     filter_backends = (DjangoFilterBackend,)
#
#
# class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
