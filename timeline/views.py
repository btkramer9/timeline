from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout


def home(request):

	context = {
		'user': request.user,
		'request': request,
	}

	return render(request, 'events/home.html', context)

def profile(request):

	context = {
		'user': request.user,
		'request': request,
	}

	return render(request, 'events/profile.html', context)

def logout(request):
	auth_logout(request)
	return redirect('/')
