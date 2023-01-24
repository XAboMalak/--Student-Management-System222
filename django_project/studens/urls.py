from django.urls import path
from . import views

from .views import (MissionCreateView, MissionUpdatView, MissionDeleteView,
 ProjectCreateView, StagesCreateView, Job_TypeCreateView, TimeSheetCreateView
)

urlpatterns = [
	path("", views.index, name="index"),
	path("add/", MissionCreateView.as_view(), name="add"),
	path("edit/<int:pk>/", MissionUpdatView.as_view(), name="edit"),
	path("showTimeSheet/<int:id>", views.TimeSheet, name="showTimeSheet"),
	path("addTimeSheet/<id_>", TimeSheetCreateView.as_view(), name="addTimeSheet"),
	path("delete/<int:pk>/", MissionDeleteView.as_view(), name="delete"),
	path("add_Project/", ProjectCreateView.as_view(), name="add_Project"),
	path("add_Job_Type/", Job_TypeCreateView.as_view(), name="add_Job_Type"),
	path("add_Stages/", StagesCreateView.as_view(), name="add_Stages"),
	
	
	path('testing/', views.testing, name='testing'),

]
