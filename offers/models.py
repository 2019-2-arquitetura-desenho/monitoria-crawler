from django.db import models


class Discipline(models.Model):
    name = models.CharField(max_length=250)
    code = models.IntegerField()
    credits = models.CharField(max_length=250)


class Professor(models.Model):
    name = models.CharField(max_length=250)


class DisciplineClass(models.Model):
    name = models.CharField(max_length=5)
    vacancies = models.SmallIntegerField()
    discipline = models.ForeignKey(
        'Discipline',
        on_delete=models.CASCADE
    )
    shift = models.CharField(max_length=250)
    teachers = models.ManyToManyField(
        Professor,
        through='Alocation',
        through_fields=('discipline_class', 'professor'),
    )


class Alocation(models.Model):
    discipline_class = models.ForeignKey(
        'DisciplineClass', on_delete=models.CASCADE
    )
    professor = models.ForeignKey(
        'Professor',
        on_delete=models.CASCADE
    )


class Meeting(models.Model):
    discipline_class = models.ForeignKey(
        'DisciplineClass',
        on_delete=models.CASCADE
    )
    day = models.CharField(max_length=50)
    init_hout = models.TimeField()
    final_hout = models.TimeField()
    room = models.CharField(max_length=250)
