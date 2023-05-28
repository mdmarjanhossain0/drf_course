from rest_framework import serializers
from myapp.models import Article
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
