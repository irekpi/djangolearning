from . import views
from django.urls import path

app_name = 'board'

urlpatterns = [
    path('', views.board, name='board'),
    path('topic/<int:pk>/', views.topic, name='topic'),
    path('topic/<int:pk>/new/', views.new_topic, name='new_topic'),
    # path('topic/post/', views.post, name='post'),
]
