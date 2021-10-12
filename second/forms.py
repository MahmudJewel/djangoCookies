from django import forms
from second import models
from django.contrib.auth.models import User

class SUForm(forms.ModelForm):
	class Meta:
		model=User
		fields=["first_name", "last_name", "username", "password"]
		widgets={
			'password': forms.PasswordInput()
		}

	def __str__(self):
		return self.username