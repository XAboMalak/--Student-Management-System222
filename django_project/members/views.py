from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm 
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from . forms import RegisterUserForm
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models.query_utils import Q

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("index")
			
		else:
			messages.success(request, "خطاء في تسجيل الدخول ...حاول مرة اخري")
			return redirect("login")

	else:
		return render(request,"authenticate/login.html",{

			})

def logout_view(request):
	logout(request)
	messages.success(request, "تم تسجيل الخروج")
	return redirect("index")

def register_user(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password1"]
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect("index")
	else:
		form = RegisterUserForm()
	return render(request, "authenticate/register.html",{
			"form": form,
			
		})

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "registration/password_reset_email.txt"
					c = {
							"email":user.email,
							'domain':'127.0.0.1:8000',
							'site_name': 'Website',
							"uid": urlsafe_base64_encode(force_bytes(user.pk)),
							"user": user,
							'token': default_token_generator.make_token(user),
							'protocol': 'http',
						}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ("/password_reset/done/")
			messages.error(request, 'An invalid email has been entered.')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="registration/password_reset.html", context={"password_reset_form":password_reset_form})