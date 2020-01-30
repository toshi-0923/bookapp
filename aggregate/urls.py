from django.urls import path
from . import views

urlpatterns = [
        path("", views.aggre_main, name="aggre_main"),
        path("<int:num>", views.aggre_main, name="aggre_main"),
        path("index_page/<str:item>", views.index_page, name="index_page"),
        path("req", views.req, name="req"),
        path("csv_import", views.csv_import, name="csv_import"),
        ]

