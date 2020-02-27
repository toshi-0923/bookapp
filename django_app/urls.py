from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("book/", include("book.urls")),
    path("day_sum/", include("day_sum.urls")),
    path("top/", include("adtress.urls"))
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)