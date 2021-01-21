from django.forms import ModelForm
from django.contrib.auth.models import User
from store.models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
#from .models import update

class Usreg(UserCreationForm):
	# class Meta:
	# 	model = User
	# 	fields = ['username','first_name','last_name','email']
	password1= forms.CharField(widget=forms.PasswordInput(attrs=
		{'class':'form-control','placeholder':"enter password"}))
	password2= forms.CharField(widget=forms.PasswordInput(attrs=
		{'class':'form-control','placeholder':"enter confirm password"}))
	class Meta:
		model=User
		fields = ['username','email']
		widgets={
		"username":forms.TextInput(attrs={'class':'form-control','placeholder':"enter username"}),
		"email":forms.EmailInput(attrs={'class':'form-control','placeholder':"example@gmail.com"}),
		
		}

class AddProductForm(ModelForm):
	class Meta:
		model=Product
		fields='__all__'


class Upfle(ModelForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name','email']
		widgets={
		'username':forms.TextInput(attrs={'class':'form-control','readonly':True}),
		'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter first_name'}),
		'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter last_name'}),
		'email':forms.EmailInput(attrs={'class':'form-control','readonly':True}),
		}

class imagepro(forms.ModelForm):
	class Meta:
		model = update
		fields = ['age','image']
		widgets={
		'age':forms.NumberInput(attrs={'class':'form-control'})
		}