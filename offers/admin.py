from django.contrib import admin
from .models import Discipline, DisciplineClass
from .models import Professor, Alocation, Meeting


admin.site.register(Discipline)
admin.site.register(DisciplineClass)
admin.site.register(Professor)
admin.site.register(Alocation)
admin.site.register(Meeting)
