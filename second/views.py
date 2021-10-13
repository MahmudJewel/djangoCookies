from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from second import forms as SForm

def home(request):
	#value = request.COOKIES.get('visits')
	if request.COOKIES.get('visits') is not None:
		value = request.COOKIES.get('visits')
		resp = render(request,'home.html', {'value':value})
		resp.set_cookie('visits',int(value)+1)
		return resp
	else:
		return redirect('setcookies')

def setcookies(request):
	if request.user.is_authenticated:
		resp = render(request,'setcookies.html')
		resp.set_cookie('visits',1)
		return resp
	else:
		return render(request,'home.html')

def getcookies(request):
	gt=request.COOKIES.get('visits')
	context={
		'gt':gt
	}
	return render(request, 'getcookies.html',context )

def deletecookies(request):
	gt=request.COOKIES.get('visits')
	resp = render(request,'deletecookies.html', {'gt':gt})
	resp.delete_cookie('visits')
	return resp
	

def signup(request):
	snForm = SForm.SUForm()
	if request.method == 'POST':
		snForm = SForm.SUForm(request.POST)
		if snForm.is_valid():
			user=snForm.save()
			user.set_password(user.password)
			user.save()
			return redirect('/')

	context={
		'snForm':snForm,
	}
	return render(request,'signup.html', context)
