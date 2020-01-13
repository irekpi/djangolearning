from . import views
from django.urls import path

app_name = 'board'

urlpatterns = [
    path('', views.board, name='board'),
    path('topic/<int:pk>/', views.topic, name='topic'),
    path('topic/<int:pk>/new/', views.new_topic, name='new_topic'),
    path('topic/<int:pk>/<int:topic_pk>/', views.topic_posts, name='topic_posts'),
    path('topic/<int:pk>/<int:topic_pk>/new_post/', views.new_post, name='new_post'),
    # path('topic/post/', views.post, name='post'),
]
