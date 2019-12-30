from . import views
from django.urls import path

app_name = 'board'

urlpatterns = [
    path('', views.board, name='board'),
    # path('board/topic/', views.topic, name='topic'),
    # path('board/topic/post/', views.post, name='post'),
]
