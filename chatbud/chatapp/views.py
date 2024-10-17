from django.shortcuts import render

# Create your views here.
rooms =[
    {'id':1,'name':'lets learn py'},
    {'id':2,'name':'lets learn api'},
    {'id':3,'name':'lets learn design'},
]
def index(request):
    context = {'rooms':rooms}
    return render(request,'chatapp/home.html',context)

def room(request,pk):
    return render(request,'chatapp/room.html')