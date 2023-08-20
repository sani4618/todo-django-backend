from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def addtodo(request):
    if request.method=="POST":
        getId=request.POST["id"]
        getTodo=request.POST["NewToDo"]
        getUser=request.POST["userName"]
        display={"id":getId,"NewToDo":getTodo,"userName":getUser}

    return HttpResponse("invalid method")


