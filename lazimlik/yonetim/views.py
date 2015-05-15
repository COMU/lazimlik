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

def about_user(request):
	return render_to_response("about_user.html")

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
	if UserProfile.objects.get(user=request.user):
		return HttpResponseRedirect('/home')
	else:
		form = UserProfileForm(request.POST or None)
		form.fields['user'].widget = forms.HiddenInput()

		if request.POST:
			form = UserProfileForm({'user':request.user.id})
			initial_value = {'user':request.user.id,'bitirilen_is_puani':0,'teslim_edilmeyen_is':0,'yaptirilan_is_puani':0,'teslim_alinmayan_is':0,'rumuz':request.POST['rumuz']}
			form = UserProfileForm(initial_value)
			print form
			form.save()
			messages.success(request, 'Rumuz eklendi.')
			return HttpResponseRedirect('/home')

	return render_to_response("user.html", locals(), context_instance=RequestContext(request))

def isyapalim(request):
	isler = YapilacakIs.objects.all()
	return render_to_response("isyapalim.html",locals(), context_instance=RequestContext(request))

def isyapalim_user(request):
	isler = YapilacakIs.objects.all()
	return render_to_response("isyapalim_user.html",locals(), context_instance=RequestContext(request))

def is_al(request):
	return render_to_response("userdetail.html")

def search(request):
    query = request.GET['q']
    t = loader.get_template('results.html')
    c = Context({ 'query': query,})
    return HttpResponse(t.render(c))