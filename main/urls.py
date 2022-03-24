from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('ranking/', views.ranking, name='ranking'),
    path('contacto/', views.contacto, name='contacto'),
    path('resultados/',views.actualizar_resultados, name='resultados'),
    path('reiniciar-ranking/', views.reiniciar_ranking, name='reiniciar'),

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)