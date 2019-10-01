from rest_framework import serializers
from .models import Discipline, DisciplineClass
from .models import Professor, Alocation, Meeting


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'


class DisciplineClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplineClass
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class AlocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alocation
        fields = '__all__'


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'
