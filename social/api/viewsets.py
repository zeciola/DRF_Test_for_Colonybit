from social.models import Comments, Replies
from rest_framework.viewsets import ModelViewSet
from social.api.serializers import CommentsSerializer, RepliesSerializer

class CommentsViewSet(ModelViewSet):

    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class RepliesViewSet(ModelViewSet):

    queryset = Replies.objects.all()
    serializer_class = RepliesSerializer


