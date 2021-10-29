from django.http.response import JsonResponse
from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views 

# *************** GET ********
def detail(request,key):
    msg = Message.objects.get(key = key)

    return HttpResponse(msg.message)

# *************** create ********
def create(request):
    if request.method == "POST":
        key = request.POST.get("key")
        message = request.POST.get("message")

        Message.objects.create(key = key, message=message)
        return render(request,"submitted.html")

    return render(request, "create.html")


# *************** Update ********

def update(request,key):
    msg = Message.objects.filter(key = key)
    if request.method == "POST":
        key = request.POST.get("key")
        message = request.POST.get("message")
        print(key, message)
        msg.update(key = key, message=message) 
        return render(request,"submitted.html")


    return render(request, "update.html")



# *************** List Json Response ********

def getJson(request):
    msg = list(Message.objects.all().values())
    return JsonResponse(msg, safe=False)