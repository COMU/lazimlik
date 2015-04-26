from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, 'giris.html')

@login_required(login_url='/')

def logout(request):
    auth_logout(request)
    return redirect('/')