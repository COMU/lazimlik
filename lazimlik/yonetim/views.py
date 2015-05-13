# -*- coding: utf-8 -*-
from django.http import *
from django.template import Template, Context
from django.shortcuts import render_to_response, redirect, render, RequestContext, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django import forms
from .forms import YapilacakIsForm
from .forms import UserProfileForm
from .models import YapilacakIs
from .models import UserProfile


def anasayfa(request):
	return render_to_response("anasayfa.html")

def about(request):
	return render_to_response("about.html")

@login_required
def isverelim(request):

	form = YapilacakIsForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		messages.success(request, 'İş eklendi.')
		return HttpResponseRedirect('/isyapalim')

	return render_to_response("isverelim.html", locals(), context_instance=RequestContext(request))

@login_required
def user(request):
	form = UserProfileForm(request.POST or None)
	form.fields['user'].widget = forms.HiddenInput()

	if request.POST:
		form = UserProfileForm({'user':request.user.id})
		print form
		form.save()
		messages.success(request, 'Rumuz eklendi.')
		return HttpResponseRedirect('/home')

	return render_to_response("user.html", locals(), context_instance=RequestContext(request))

def isyapalim(request):
	isler = YapilacakIs.objects.all()
	return render_to_response("isyapalim.html",locals(), context_instance=RequestContext(request))