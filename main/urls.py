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
    path('me/', views.me, name='me'),
    path('ruling/', views.ruling, name='ruling'),
    path('agregar-regla/', views.add_rulings, name='agregar_regla'),
    path('modificar-regla/<id>/', views.editar_regla, name='modificar_regla'),
    path('eliminar-regla/<id>/', views.eliminar_regla, name='eliminar_regla'),
    path('regla-info/<id>/', views.ruling_individual, name='regla_info'),
    path('about-us', views.about_us, name='about'),

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)