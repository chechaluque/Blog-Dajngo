from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)
from posts.models import Post


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields =[
            'title',
            #'slug',
            'content',
            'publish'
        ]
post_url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='slug'
    )
class PostListSerializer(ModelSerializer):
    url = post_url
    user = SerializerMethodField()
    class Meta:
        model = Post
        fields =[
            'url',
            'user',
            'title',

            'content',
            'publish',

        ]
    def get_user(self, obj):
        return str(obj.user.username)


class PostDetailSerializer(ModelSerializer):
    url = post_url
    user = SerializerMethodField()
    image = SerializerMethodField()
    html = SerializerMethodField()
    class Meta:
        model = Post
        fields =[
            'url',
            'user',
            'id',
            'title',
            'slug',
            'content',
            'html',
            'publish',
            'image'
        ]
    def get_html(self, obj):
        return obj.get_markdown()

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image