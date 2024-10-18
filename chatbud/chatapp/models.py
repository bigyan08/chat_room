from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# a topic can have multiple rooms, but a room can have a single topic
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    #participants
    updated = models.DateTimeField(auto_now=True) # auto_now picks the time when the new data gets updated
    created = models.DateTimeField(auto_now_add=True) # whereas, auto_now_add saves the time when the data is created, hence it stays same for a particular data.

    def __str__(self):
        return self.name

# here we are gonna create a message model, which will be one to many relation where a user can create many messages
class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE) #on_delete=models.CASCADE ensures that when a room is deleted then the messages gets deleted as well.
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50] #this will provide only the preview of the body and not all the contents.