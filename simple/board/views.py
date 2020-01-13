from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Board, Topic, Post
from .forms import NewTopicForm, NewPostForm


#class BoardView(Board):
    #template_name = 'board.html'

def board(request):
    boards = Board.objects.all()
    return render(request, 'board.html', {'boards': boards})


def topic(request, pk):
    try:
        board = Board.objects.get(pk=pk)
        board_id = id(board)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topic.html', {'board': board,
                                          'board_id': board_id})

# new topic without class
# def new_topic(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     if request.method == "POST":
#         subject = request.POST['subject']
#         message = request.POST['message']
#
#         user = User.objects.first()  # TODO: get the currently logged in user
#
#         topic = Topic.objects.create(subject=subject, board=board, starter=user)
#         post = Post.objects.create(message=message, topic=topic, created_by=user)
#         return redirect('board:topic', pk=board.pk) # TODO: redirect to the created topic page)
#     return render(request, 'new_topic.html', {'board': board})


@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            Post.objects.create(message=form.cleaned_data.get('message'), topic=topic, created_by=request.user)
            return redirect('board:topic', pk=board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board,
                                              'form': form})


def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    topic.views += 1
    topic.save()
    return render(request, 'topic_posts.html', {'topic': topic})


@login_required
def new_post(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('board:topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {'topic': topic,
                                             'form': form})

