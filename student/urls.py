from django.urls import path

from . import views

urlpatterns = [
    path('enrollment/select', views.select_curriculum),
]
