from rest_framework import serializers
from myapp.models import (
    Article,
    Image,
    Book
)
from drf_extra_fields.fields import Base64ImageField


class ArticleBase64Serilizer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Article
        fields = ["title", "content", "image"]

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["title", "content", "image"]



class ImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=True)
    class Meta:
        model = Image
        fields = ('title', 'image')

class BookSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Book
        fields = ('name', 'description', 'images')

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        book = Book.objects.create(**validated_data)
        
        for image_data in images_data:
            print(image_data)
            image_obj = Image.objects.create(**image_data)
            book.images.add(image_obj)

        return book


from rest_framework import serializers
from myapp.models import ResizableImage
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class ResizableImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResizableImage
        fields = ('title', 'original_image', 'resized_image')

    def create(self, validated_data):
        print(validated_data)
        instance = super().create(validated_data)
        original_image = validated_data.pop('original_image')

        # Resize the image
        resized_image = self.resize_image(original_image)
        instance.resized_image.save(original_image.name, ContentFile(resized_image), save=False)
        instance.save()

        return instance

    def resize_image(self, image):
        img = Image.open(image)
        # Resize the image to a desired size (e.g., 300x300)
        resized_img = img.resize((300, 300), resample=Image.BICUBIC)

        # Convert the resized image to bytes
        buffer = BytesIO()
        resized_img.save(buffer, format='png')
        img_bytes = buffer.getvalue()

        return img_bytes
