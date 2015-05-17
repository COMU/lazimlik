# -*- coding: utf-8 -*-
from django.http import *
from django.template import Template, Context
from django.shortcuts import render_to_response, redirect, render, RequestContext, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django import forms
from forms import UserProfileForm, IsForm
from models import UserProfile, Is, Sehir


def anasayfa(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/home")
	workers = UserProfile.objects.all().order_by("bitirilen_is_puani")    
	return render_to_response("anasayfa.html", locals(), context_instance=RequestContext(request))

def about(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/about_user")
	return render_to_response("about.html")

@login_required
def about_user(request):
	return render_to_response("about_user.html")

@login_required
def is_olustur(request):
	form = IsForm()
	if request.POST:
		initial_value = {'olusturan_kullanici': request.user,
						 'tanim': request.POST['tanim'],
						 'baslangic_tarihi': request.POST['baslangic_tarihi'],
						 'bitis_tarihi': request.POST['bitis_tarihi'],
						 'detay': request.POST['detay']
						 #TODO 'etiketler': request.POST['etiketler'],
						}
		form = IsForm(initial_value)
		if form.is_valid():
			_is = form.save(commit=False)
			_is.olusturan_kullanici = request.user
			_is.save()
			messages.success(request, 'İş eklendi.')
			return HttpResponseRedirect("/isyapalim_user")
		else:
			#TODO form valid degilse ne yapmak lazim?
			pass
	else:	
		return render_to_response("isverelim.html", locals(), context_instance=RequestContext(request))

@login_required
def profil_olustur(request):
	if request.POST:
		initial_value = {'user':request.user.id,
						 'bitirilen_is_puani':0,
						 'teslim_edilmeyen_is':0,
						 'yaptirilan_is_puani':0,
						 'teslim_alinmayan_is':0, 
						 'verdigi_isler':None, 
						 'aldigi_isler':None, 
						 'rumuz':request.POST['rumuz']}
		form = UserProfileForm(initial_value)
		print form
		form.save()
		messages.success(request, 'Rumuz eklendi.')
		return HttpResponseRedirect('/home')
	else:
		if UserProfile.objects.filter(user=request.user).count() > 0:
			return HttpResponseRedirect('/home')
		else:
			form = UserProfileForm(request.POST or None)
			form.fields['user'].widget = forms.HiddenInput()
			return render_to_response("user.html", locals(), context_instance=RequestContext(request))


def is_goruntule(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/isyapalim_user")
	isler = Is.objects.all()
	return render_to_response("is_goruntule.html", locals(), context_instance=RequestContext(request))

@login_required
def isyapalim_user(request):
	isler = Is.objects.all()
	return render_to_response("isyapalim_user.html", locals(), context_instance=RequestContext(request))

def is_al(request, is_id):
	try:
		_is = Is.objects.get(id=is_id)
		_is.isi_yapan_kullanici = request.user
		_is.save()
		form = IsForm.objects.filter(isi_yapan_kullanici=request.user)
		return render_to_response("userdetail.html")
	except Exception:
		print "hata olustu"
		isler = Is.objects.all()
		return render_to_response("isyapalim_user.html", locals(), context_instance=RequestContext(request))

def search(request):
	query = request.GET['q']
	t = loader.get_template('results.html')
	c = Context({ 'query': query,})
	return HttpResponse(t.render(c))

def results(request):
	return render_to_response("results.html")
