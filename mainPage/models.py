from django.db import models

# Create your models here.
allUsers = []
class User(models.Model):
    identification = models.CharField(max_length = 10)
    name = models.CharField(max_length = 250)
    #connected = BooleanField()



class Connection(models.Model):
    Location = models.CharField(max_length = 250)


def makeUser(phoneNum):
    allUsers.append(phoneNum)

def FHandler(View):
    def get(self, request, *args, **kwargs):
        return HTTPResponse("Get request");
    def post(self, request, *args, **kwargs):
        return HTTPResponse("Post request")