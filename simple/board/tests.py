from django.urls import reverse, resolve
from django.test import TestCase
from simple import views



class BoardTest(TestCase):
    def test_board_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    # def test_board_url_resolves_home_view(self):
    #     view = resolve('/')
    #     self.assertEquals(views.HomeView, home)

# class TopicTest(TestCase):
#     def setUp(self):
#         Board.object.create(name='Django', description='Django board')
#
#
#     def test_topic_view_success_status_code(self):
#         url = reverse('topic', kwargs={'pk': 1})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
# from django.contrib.auth.models import User
# from django.test import TestCase
# from django.urls import resolve, reverse
#
# from ..models import Board, Post, Topic
# from ..views import topic_posts
#
#
# class TopicPostsTests(TestCase):
    # def setUp(self):
    #     board = Board.objects.create(name='Django', description='Django board.')
    #     user = User.objects.create_user(username='john', email='john@doe.com', password='123')
    #     topic = Topic.objects.create(subject='Hello, world', board=board, starter=user)
    #     Post.objects.create(message='Lorem ipsum dolor sit amet', topic=topic, created_by=user)
    #     url = reverse('topic_posts', kwargs={'pk': board.pk, 'topic_pk': topic.pk})
    #     self.response = self.client.get(url)