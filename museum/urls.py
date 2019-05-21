from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exhibit/<int:exhibit_pk>', views.exhibit, name='exhibit'),
    path('exhibit/<int:exhibit_pk>/object/<int:object_pk>', views.object, name='object'),
]
