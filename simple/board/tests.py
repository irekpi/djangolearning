from django.urls import reverse
from django.test import TestCase


class BoardTest(TestCase):
    def test_board_view_status_code(self):
        url = reverse('board.board')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    def test_board_url_resolves_board_view(self):
        view = resolve('/')
        self.assertEquals(view.func, board)