from django.shortcuts import render
from .models import Board


#class BoardView(Board):
    #template_name = 'board.html'

def board(request):
    boards = Board.objects.all()
    return render(request, 'board.html', {'boards': boards})

