from django.urls import path
from . import views

app_name = 'ukemenyscraper'
urlpatterns = [
    path('', views.ukensmatprat, name='ukensmatprat'),
]
