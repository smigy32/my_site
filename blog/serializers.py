import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = "__all__"


# class PostModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=150)
#     content = serializers.CharField()
#     excerpt = serializers.CharField(max_length=200)
#     date = serializers.DateField(read_only=True)
#     author_id = serializers.IntegerField()
#     slug = serializers.SlugField(read_only=True)

#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.excerpt = validated_data.get("excerpt", instance.excerpt)
#         instance.date = validated_data.get("date", instance.date)
#         instance.author_id = validated_data.get("author_id", instance.author_id)
#         instance.slug = validated_data.get("slug", instance.slug)
#         instance.save()
#         return instance


# def encode():
#     post = PostModel("Some Title", "Some Content")
#     model_sr = PostSerializer(post)
#     print(model_sr.data, type(model_sr.data), sep="\n")
#     json = JSONRenderer().render(model_sr.data)
#     print(json)


# def decode():
#     stream = io.BytesIO(b'{"title":"Some Title","content":"Some Content"}')
#     data = JSONParser().parse(stream)
#     serializer = PostSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
