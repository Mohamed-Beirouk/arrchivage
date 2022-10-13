from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drf_spectacular.views import SpectacularAPIView,SpectacularRedocView,SpectacularSwaggerView

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apis.urls', namespace='apis')),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc",),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
