from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exhibit/<int:pk>', views.exhibit, name='exhibit'),
    path('object/<int:pk>', views.object, name='object'),
]
