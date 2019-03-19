from django.db import models
from django.contrib.auth.models import User

class Comments(models.Model):

    comment = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    likes_comments = models.BigIntegerField()
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class Replies(models.Model):

    comments_id = models.ForeignKey(Comments, on_delete=models.CASCADE)
    comments_reply = models.TextField()
    likes_reply = models.BigIntegerField()
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comments_reply

