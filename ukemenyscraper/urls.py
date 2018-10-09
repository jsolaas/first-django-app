from django.urls import path
from . import views


urlpatterns = [
    path('', views.ukensmatprat, name='ukensmatprat'),
]
