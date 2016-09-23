from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)
from posts.models import Post
from comments.api.serializers import CommentSerializer
from comments.models import Comment

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
    comments = SerializerMethodField()
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
            'image',
            'comments',
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
    def get_comments(self, obj):
        content_type = obj.get_content_type
        object_id = obj.id
        c_qs =Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments
