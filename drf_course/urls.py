from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from myapp.api.views import (
    upload_article_api_view,
    base64_image_upload_api_view,

    # Image with nested json
    BookAPIView,
    book_api_view,
    ResizableImageAPIView
)

from myapp.views import upload_image_view, upload_base64_image_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/base64_image_upload",
        base64_image_upload_api_view,
        name="base64_image_upload",
    ),
    path("api/upload_article", upload_article_api_view, name="api_upload_article"),
    path("upload_image", upload_image_view, name="upload_image"),
    path("base64_image", upload_base64_image_view, name="base64_image"),


    # Image with nested json
    path("api/image-with-nested-json", BookAPIView.as_view(), name="image-with-nested-json"),
    path("api/image-with-nested-json-function", book_api_view, name="image-with-nested-json-function"),
    path("api/resizable-image", ResizableImageAPIView.as_view(), name="resizable-image")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
