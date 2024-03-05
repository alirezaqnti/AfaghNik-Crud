from django.http import Http404
from rest_framework import viewsets

from Main.models import Dataset
from Main.serializers import DatasetSerializer


class DatasetViewSet(viewsets.ModelViewSet):
    serializer_class = DatasetSerializer
    queryset = Dataset.objects.all()
