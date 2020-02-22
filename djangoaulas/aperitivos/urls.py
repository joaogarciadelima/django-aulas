from django.urls import path

from djangoaulas.aperitivos.views import video, indice

app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
    path('', indice, name='indice')
]
