# -*- coding: utf-8 -*-
from django.http import *
from django.template import Template, Context
from django.shortcuts import render_to_response, redirect, render, RequestContext, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import yapilacakIsForm
from .forms import kullaniciForm
from .models import yapilacakIs

def anasayfa(request):
    return render_to_response("anasayfa.html")

@login_required
def isverelim(request):

	form = yapilacakIsForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		messages.success(request, 'İş eklendi.')
		return HttpResponseRedirect('/')

	return render_to_response("isverelim.html", locals(), context_instance=RequestContext(request))

def user(request):

	form = kullaniciForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		messages.success(request, 'Rumuz eklendi.')
		return HttpResponseRedirect('/home')

	return render_to_response("user.html", locals(), context_instance=RequestContext(request))

def isyapalim(request):
	isler = yapilacakIs.objects.all()
    	return render_to_response("isyapalim.html",locals(), context_instance=RequestContext(request))
