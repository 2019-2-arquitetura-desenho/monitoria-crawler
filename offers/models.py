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
        Discipline,
        related_name = 'discipline_class',
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
        DisciplineClass,
        related_name = 'meetings',
        on_delete=models.CASCADE
    )
    day = models.CharField(max_length=50)
    init_hour = models.TimeField()
    final_hour = models.TimeField()
    room = models.CharField(max_length=250)
