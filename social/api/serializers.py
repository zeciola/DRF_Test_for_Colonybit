from social.models import Comments, Replies
from rest_framework import serializers

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id','comment','user_id',
                  'likes_comments','create_at',
                  'update_at'
                  )


class RepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replies
        fields = ('id','comments_id','comments_reply',
                  'likes_reply','create_at','update_at'
                  )