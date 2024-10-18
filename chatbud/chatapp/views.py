from django.shortcuts import render
from .models import Room

# Create your views here.
def index(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'chatapp/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room} 
    return render(request,'chatapp/room.html',context)