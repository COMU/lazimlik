# -*- coding: utf-8 -*-
from django.http import *
from django.template import Template, Context
from django.shortcuts import render_to_response, redirect, render, RequestContext, HttpResponseRedirect
from django.contrib import messages

from .forms import yapilacakIsForm

def anasayfa(request):
    return render_to_response("anasayfa.html")

def isverelim(request):

	form = yapilacakIsForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		messages.success(request, 'İş eklendi.')
		return HttpResponseRedirect('/')
		
	return render_to_response("isverelim.html", locals(), context_instance=RequestContext(request))

def isyapalim(request):
    return render_to_response("isyapalim.html")
