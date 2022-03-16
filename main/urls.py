from django.urls import path
from . import views
from django.conf.urls import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('ranking/', views.ranking, name='ranking'),
]