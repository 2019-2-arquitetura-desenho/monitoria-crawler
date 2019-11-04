from rest_framework import viewsets, mixins
from .serializers import DisciplineSerializer
from .models import Discipline


class DisciplineViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    filter_fields = ['code']
