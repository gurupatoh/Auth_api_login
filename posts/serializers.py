from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            "id",
            "author",
            "body",
            "created_at"

        )
        model =Post
 