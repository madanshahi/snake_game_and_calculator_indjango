from django.shortcuts import render

def move_snake(request):
    return render(request,'snake/snake.html')
def endGame(request):
    return render(request,'end.html')
