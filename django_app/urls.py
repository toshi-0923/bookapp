from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("book/", include("book.urls")),
    path("day_sum/", include("day_sum.urls")),
    ]
