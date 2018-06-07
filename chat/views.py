from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
#...


@login_required
def index(request):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Render that in the index template
    roo = Room.objects.order_by("title")
    return render(request, "index.html" ,{"rooms": roo,})




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