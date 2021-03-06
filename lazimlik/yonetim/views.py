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

from models import Document
from forms import DocumentForm

def anasayfa(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/home")   
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
		olusturan = UserProfile.objects.get(user__id=request.user.id)
		initial_value = {'olusturan_kullanici': olusturan,
						 'tanim': request.POST['tanim'],
						 'baslangic_tarihi': request.POST['baslangic_tarihi'],
						 'bitis_tarihi': request.POST['bitis_tarihi'],
						 'detay': request.POST['detay'],
						 'sehir': request.POST['sehir'],
						 #TODO 'etiketler': request.POST['etiketler'],
						 'status': 1
						}
		form = IsForm(initial_value)
		if form.is_valid():
			_is = form.save(commit=False)
			_is.olusturan_kullanici = UserProfile.objects.get(user__id=request.user.id)
			_is.save()
			messages.success(request, 'İş eklendi.')
			return HttpResponseRedirect("/isyapalim_user")
		else:
			#TODO form valid degilse ne yapmak lazim?
			pass
	else:
		file = open('data/sehir.txt', 'r')
		for i in file.readlines():
			try:
				sehir = Sehir.objects.get(sehir_adi=i)
			except Exception:
				sehir = Sehir(sehir_adi=i)
				sehir.save()	
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
						 'rumuz':request.POST['rumuz'],
						 'status': 1}
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
	isler = Is.objects.filter(teslim_edildi = False)
	return render_to_response("is_goruntule.html", locals(), context_instance=RequestContext(request))

@login_required
def isyapalim_user(request):
	isler = Is.objects.filter(teslim_edildi = False, status = 1)
	return render_to_response("isyapalim_user.html", locals(), context_instance=RequestContext(request))

@login_required
def is_al(request, is_id):
	try:
		_is = Is.objects.get(id=is_id)
		_is.isi_yapan_kullanici = UserProfile.objects.get(user__id=request.user.id)
		_is.status = 2
		_is.save()
		return render_to_response("is_al.html", locals(), context_instance=RequestContext(request))
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))
		isler = Is.objects.all()
		return render_to_response("isyapalim_user.html", locals(), context_instance=RequestContext(request))

@login_required
def is_teslim_et(request, is_id):
	isno = Is.objects.get(id=is_id)
	if request.method == 'POST':
		teslim = Is.objects.get(id=is_id)
		teslim.teslim_edildi = True
		teslim.status = 3 
		teslim.save()

		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			try:
				newdoc = Document.objects.get(isid=is_id)
				newdoc.docfile = request.FILES['docfile']
				newdoc.save()
			except Document.DoesNotExist:
				newdoc = Document(docfile = request.FILES['docfile'])
				newdoc.isid = Is.objects.get(id=is_id)
				newdoc.save()

			return HttpResponseRedirect("/teslim_edildi")
	else:
		form = DocumentForm()

	documents = Document.objects.all()

	return render_to_response("is_teslim_et.html", locals(), context_instance=RequestContext(request))

@login_required
def is_havuzu(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'])
			newdoc.save()

			return HttpResponseRedirect("/home")
	else:
		form = DocumentForm()

	documents = Document.objects.all()

	return render_to_response("is_havuzu.html", locals(), context_instance=RequestContext(request))

@login_required
def userdetail(request):
	kullanici = UserProfile.objects.filter(user=request.user)
	return render_to_response("userdetail.html", locals(), context_instance=RequestContext(request))

@login_required
def alinan_isler(request):
	isi_yapan = UserProfile.objects.get(user__id=request.user.id)
	islist = Is.objects.filter(teslim_edildi = False, isi_yapan_kullanici=isi_yapan, status = 2)
	return render_to_response("alinan_isler.html", locals(), context_instance=RequestContext(request))

@login_required
def teslim_edildi(request):
	return render_to_response("teslim_edildi.html")

@login_required
def teslim_edilen_is(request):
	yapilan = Document.objects.filter(isid__status = 3)
	return render_to_response("teslim_edilen_is.html", locals(), context_instance=RequestContext(request))

@login_required
def onaylandi(request, is_id):
	onay = Is.objects.get(id=is_id)
	onay.status = 4 
	onay.save()
	return render_to_response("onaylandi.html")

@login_required
def reddedildi(request, is_id):
	onay = Is.objects.get(id=is_id)
	onay.status = 1 
	onay.teslim_edildi = False
	onay.save()
	return render_to_response("reddedildi.html")
