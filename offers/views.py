from rest_framework import viewsets
from .serializers import DisciplineSerializer, DisciplineClassSerializer
from .serializers import ProfessorSerializer, AlocationSerializer, MeetingSerializer


class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer


class DisciplineClassViewSet(viewsets.ModelViewSet):
    queryset = DisciplineClass.objects.all()
    serializer_class = DisciplineClassSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class AlocationViewSet(viewsets.ModelViewSet):
    queryset = Alocation.objects.all()
    serializer_class = AlocationSerializer


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
