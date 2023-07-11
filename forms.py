# from typing_extensions import Required
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField,PasswordChangeForm,PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import password_changed
from django.core.exceptions import RequestDataTooBig
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.fields import Field
from django.forms import widgets
from django.forms.fields import ChoiceField
from .models import Customer,STATE_CHOICE


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
	    model = User
	    fields = ["username", "email", "password1", "password2"]



class LoginForm(AuthenticationForm):
	username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'clas':'form-control'}))
	password = forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'})

	
 
class MyPasswordChange(PasswordChangeForm):
	pass


class ProfileForm(forms.ModelForm):
	class Meta:
		model= Customer
		fields=['name','locality','city','state','zipcode']
		widgets={'name':forms.TextInput(attrs={'class':"form-control"}),'locality':forms.TextInput( attrs={'class':"form-control"}),'city':forms.TextInput(attrs={'class':"form-control"}),'state':forms.TextInput(attrs={'class':"form-control"}),'zipcode':forms.NumberInput(attrs={'class':"form-control"})}

