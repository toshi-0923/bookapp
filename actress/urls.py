from django.urls import path
from . import views

app_name = "actress"
urlpatterns = [
        path("", views.index, name="index"),
        path("create", views.create_actress, name="create_actress"),
        path("cast_page<int:item>", views.cast_page, name="cast_page"),
        path("cast_edit<int:item>", views.cast_edit, name="cast_edit"),
        ]

