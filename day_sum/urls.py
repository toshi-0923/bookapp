from django.urls import path
from . import views

urlpatterns = [
        path("", views.main, name="main"),
        path("day_edit/<int:num>", views.day_edit, name="day_edit"),
        ]