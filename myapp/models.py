from django.db import models


def file_location(instance, filename, **kwargs):
    file_path = f"article/{instance.title}-{filename}"
    return file_path


class Article(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(max_length=5000, null=False, blank=False)
    image = models.ImageField(upload_to=file_location, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")

    def __str__(self):
        return self.title
