from rest_framework import serializers
from .models import Discipline, DisciplineClass
from .models import Professor, Meeting


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['name']


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ['day', 'init_hour', 'final_hour', 'room']


class DisciplineClassSerializer(serializers.ModelSerializer):
    teachers = ProfessorSerializer(many=True, read_only=True)
    meetings = MeetingSerializer(many=True, read_only=True)

    class Meta:
        model = DisciplineClass
        fields = ['name', 'vacancies', 'shift', 'teachers', 'meetings']

class DisciplineSerializer(serializers.ModelSerializer):
    discipline_class = DisciplineClassSerializer(many=True, read_only=True)

    class Meta:
        model = Discipline
        fields = ['name', 'code', 'discipline_class']
