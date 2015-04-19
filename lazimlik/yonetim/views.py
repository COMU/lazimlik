# -*- coding: utf-8 -*-
from django.http import *
from django.template import Template, Context
from django.shortcuts import render_to_response, redirect, render

def anasayfa(request):
    return render_to_response('anasayfa.html')

def isverelim(request):
    return render_to_response('isverelim.html')

def isyapalim(request):
    return render_to_response('isyapalim.html')
