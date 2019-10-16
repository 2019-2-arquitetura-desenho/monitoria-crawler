"""crawler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from offers.views import DisciplineViewSet, DisciplineClassViewSet
from offers.views import ProfessorViewSet, AlocationViewSet, MeetingViewSet


router = routers.DefaultRouter()
router.register(r'discipline', DisciplineViewSet)
router.register(r'disciplineclass', DisciplineClassViewSet)
router.register(r'professor', ProfessorViewSet)
router.register(r'alocation', AlocationViewSet)
router.register(r'meeting', MeetingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
