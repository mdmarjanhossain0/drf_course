from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from myapp.api.views import upload_article_api_view, base64_image_upload_api_view

from myapp.views import upload_image_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/base64_image_upload",
        base64_image_upload_api_view,
        name="base64_image_upload",
    ),
    path("api/upload_article", upload_article_api_view, name="api_upload_article"),
    path("upload_image", upload_image_view, name="upload_image"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
