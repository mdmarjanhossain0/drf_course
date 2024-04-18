from django.contrib import admin

from myapp.models import (
    Article,
    Image,
    Book,
    ResizableImage
)

admin.site.register(Article)
admin.site.register(Image)
admin.site.register(Book)
admin.site.register(ResizableImage)