from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import *
from django.template import Template, Context
from django.shortcuts import render_to_response, redirect, render, RequestContext, HttpResponseRedirect

def login(request):
    return render(request, 'login.html')

@login_required

def home(request):
	u = request.user
	return render_to_response("home.html", locals(), context_instance=RequestContext(request))

def logout(request):
    auth_logout(request)
    return redirect('/')