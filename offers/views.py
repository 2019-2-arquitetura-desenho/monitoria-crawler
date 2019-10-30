from rest_framework import viewsets
from .serializers import DisciplineSerializer
from .models import Discipline


class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    filter_fields = ['code']
