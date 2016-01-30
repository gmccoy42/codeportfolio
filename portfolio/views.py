from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import projects
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from datetime import datetime
import time
from django.utils.timezone import utc
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.hashers import make_password
import os

def index(request):
	if request.method == 'POST':
		try:
			user = authenticate(username=request.POST['userName'], password=request.POST['userPassword'])
			if user is not None:
		    	# the password verified for the user
				if user.is_active:
					auth_login(request, user)
					print("User is valid, active and authenticated")
				else:
					print("The password is valid, but the account has been disabled!")
			else:
			    # the authentication system was unable to verify the username and password
				print("The username and password were incorrect.")
				messages.error(request, "The username and password were incorrect.")
		except Exception:
			print("Post error")	
	if request.user.is_authenticated():
		stories = []
		paginator = Paginator(stories,20)
		page = request.GET.get('page')
		try:
			stories = paginator.page(page)
		except PageNotAnInteger:
			stories = paginator.page(1)
		except EmptyPage:
			stories = paginator.page(paginator.num_pages)
	else:
		stories = None

	return render(request, 'main.html', {'stories': stories })

def register(request):
	if request.method == 'POST':
		u = None
		try:
			u = User.objects.create(username=request.POST["username"], password=make_password(request.POST["userpassword"], salt=None, hasher='default'), email=request.POST["email"])
			u.save()
			#messages.error(request, "I SAID GO AWAY")
		except Exception as e:
			print(e)
			messages.error(request, "Invalid Request, register failed")
	return render(request, "main.html", {'stories': None })


def add(request):
    if request.user.is_authenticated():
        print(request.POST)
        if request.method == 'POST':
            s = projects.objects.create(
                url=request.POST.get("link", ""), 
                name=request.POST.get("name", ""), 
                user=request.user, 
                description=request.POST.get("description", ""), 
                language=request.POST.get("language", ""),
                display_type=request.POST.get("type", "")
            )
            s.save()
        sites = projects.objects.filter(user=request.user).all()
    else:
        sites = None
    return render(request, 'add.html', {'sites':sites})
