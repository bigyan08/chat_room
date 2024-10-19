from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

# Create your views here.
def index(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'chatapp/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room} 
    return render(request,'chatapp/room.html',context)

#now we are gonna create CRUD functionalities for the user to create room connecting to room_form template.
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form':form}
    return render(request,'chatapp/room_form.html',context)


def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request,'chatapp/room_form.html',context)


def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('index')
    return render(request,'chatapp/delete.html',{'obj':room})