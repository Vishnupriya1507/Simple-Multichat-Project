from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
import string
import random
import json

#...
def group_code_generator(size=5, chars=string.ascii_uppercase + string.digits):
    str = ''.join(random.choice(chars) for _ in range(size))
    for grp in Room.objects.all():
        if grp.title == str:
            str = group_code_generator()
    return str

@login_required
def index(request):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Render that in the index template
    roo = Room.objects.order_by("title")
    return render(request, "index.html" ,{"rooms": roo,})


@login_required
def create_room(request):
    room = Room()
    room.title = "bdcbd"
    room.save()
    return HttpResponseRedirect('/')




@login_required
def create_group(request):
    room = Room()
    room.types = "Closed"
    room.title = group_code_generator()
    room.save()
    resp = {"groupCode":room.title}
    return JsonResponse(resp)


@login_required
def create_open_group(request):
    try:
        room = Room()
        room.types = "Open"
        room.title = group_code_generator()
        room.save()
    except:
        Room.objects.filter(types="Open").get(status=1)
        room = Room.objects.filter(types="Open").get(status=1)
    resp = {"groupCode":room.title}
    return JsonResponse(resp)
"""
@login_required
def home(request):
    return render(request, "home.html" )



@login_required
def logout(request):
    return HttpResponseRedirect('/')



@login_required
def login(request):
    return render(request, "login.html" )

"""