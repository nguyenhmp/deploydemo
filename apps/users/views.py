# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(req):
	if req.method == "POST":
		print req.POST
		User.objects.create(first_name=req.POST["first_name"], last_name=req.POST["last_name"], email=req.POST["email"], password=req.POST["password"], username=req.POST["username"])
		return redirect('/users')
	else:
		context = {
			"all_users":User.objects.all()
		}
		return render(req, "users/index.html", context)

def update(req, user_id):
	if req.method == "POST":
		user = User.objects.get(id=user_id)
		user.first_name = req.POST["first_name"]
		user.last_name = req.POST["last_name"]
		user.email = req.POST["email"]
		user.username = req.POST["username"]
		user.password = req.POST["password"]
		user.save()
		return redirect('/users')
	else:
		context = {
			"user":User.objects.get(id=user_id)
		}
		return render(req, "users/show.html", context)

def edit(req, user_id):
	context = {
		"user":User.objects.get(id=user_id)
	}
	return render(req, "users/edit.html", context)
def new(req):
	return render(req, 'users/new.html')