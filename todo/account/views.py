from django.shortcuts import render, redirect
from .forms import RegisterForm



def register(response):

	form = RegisterForm()

	if response.method == 'POST':
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			return redirect("/") 
		else:
			form = RegisterForm()
	
	return render(response, "registration/signup.html", {"form":form})