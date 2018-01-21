from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

db = {"null":{"exists":False, "active":False, "longitude":"-1.0",
        "latitude":"-1.0"},
        "911":{"exists":True, "active":True,
            "longitude":"-82.3440538",
            "latitude":"29.6480567"}}
# Create your views here.
@csrf_exempt
def index(request):
    print(request)
    if (request.method=="GET"):
        print(db)
        num = request.GET.get("number")
        if num not in db:
            return HttpResponse(json.dumps(db["null"]))
        return HttpResponse(json.dumps(db[num]))

    if request.method=="POST":
        db[request.POST.get("number", "")] = {
            "longitude":request.POST.get("longitude", ""),
            "latitude":request.POST.get("latitude", ""),
            "active": True,
            "exists": True
        }
        


        return HttpResponse("OK");
    return HttpResponse("<h1>This is the Main page<h1>")
