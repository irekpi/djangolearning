from django.urls import reverse, resolve
from django.test import TestCase
from .models import Board


# class BoardTest(TestCase):
#     def test_board_view_status_code(self):
#         url = reverse('board.board')
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
#
#     def test_board_url_resolves_board_view(self):
#         view = resolve('/')
#         self.assertEquals(view.func, board)

# class TopicTest(TestCase):
#     def setUp(self):
#         Board.object.create(name='Django', description='Django board')
#
#
#     def test_topic_view_success_status_code(self):
#         url = reverse('topic', kwargs={'pk': 1})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
