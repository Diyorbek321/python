from django.shortcuts import render

# Create your views here.
rooms = [
    {'id': 1, 'name': 'lets learn python'},
    {'id': 2, 'name': 'lets'},
    {'id': 3, 'name': 'learn python'},
    {'id': 4, 'name': 'python'}
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room:': room}
    return render(request, 'base/room.html')
