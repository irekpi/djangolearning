from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.utils.text import Truncator


class Board(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_post_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()


class Topic(models.Model):
    subject = models.CharField(max_length=100)
    last_update = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name="topics", on_delete=CASCADE)
    starter = models.ForeignKey(User, related_name="topics", on_delete=CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, related_name="posts", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name="post", on_delete=CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name="+", on_delete=CASCADE)

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)

