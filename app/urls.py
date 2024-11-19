from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ConsultaView.as_view(), name='livros'),
    path('reserva/', ReservaView.as_view(),
name='reserva'),
    path('delete/<int:id>/', DeleteLivroView.as_view(),
name='delete'),
]

path('editar/<int:id>/', EditarLivroView.as_view(), name='editar'),