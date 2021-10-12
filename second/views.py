from django.shortcuts import render, redirect
from second import forms as SForm

def home(request):
	
	return render(request,'home.html')

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
