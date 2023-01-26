from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime

class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(label="البرييد الالكتروني", widget=forms.EmailInput(attrs={"class":"form-control"}))
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)
		self.fields["username"].widget.attrs["class"] = "form-control"
		self.fields["password1"].widget.attrs["class"] = "form-control"
		self.fields["password2"].widget.attrs["class"] = "form-control"