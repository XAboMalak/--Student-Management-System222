from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	path("login", views.login_user, name='login'),
	path("logout", views.logout_view, name='logout'),
	path("register/", views.register_user, name='register'),
	path("password_reset/", views.password_reset_request,name="password_reset"),

	# path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

	]