from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exhibit/<int:pk>', views.exhibit, name='exhibit'),
    path('exhibit/<int:exhibit_pk>/<int:obj_num>', views.object, name='object'),
]
