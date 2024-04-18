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

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='book_images/')

class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ManyToManyField(Image)


class ResizableImage(models.Model):
    title = models.CharField(max_length=255)
    original_image = models.ImageField(upload_to='original_images/')
    resized_image = models.ImageField(upload_to='resized_images/', null=True, blank=True)
