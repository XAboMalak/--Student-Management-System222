from django.shortcuts import render
from django.urls import reverse_lazy
from . models import Projects, Mission, Stages, Job_Type, MissionTimeSheet, working_lisence_year,igama_year,insurance,electric,cars
import datetime
from . forms import MissionForm, MissionTimeSheetForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from easy_select2 import select2_modelform

def index(request):#[:10]
	x = datetime.date.today().month
	y = datetime.date.today().year
	input_month = x if ((request.POST.get("input_month", False)) == 0) else  request.POST.get("input_month", False)
	input_year = y if ((request.POST.get("input_year", False))== 0) else request.POST.get("input_year", False)
	return render(request, "studens/index.html", {
		"Mission": Mission.objects.filter(finish_Date__year=input_year).filter(finish_Date__month=input_month).order_by("project_Name", "-finish_Date"), 
		})

class MissionCreateView(LoginRequiredMixin, CreateView):
	model = Mission
	form_class = MissionForm
	template_name = "studens/add.html"
	login_url = "login" # this for LoginRequiredMixin

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)

class MissionUpdatView(LoginRequiredMixin, UpdateView):
	model = Mission
	form_class = MissionForm
	template_name = "studens/edit.html"
	login_url = "login" # this for LoginRequiredMixin
	 
	def form_valid(self, form):
		form.instance.updated_by = self.request.user.username
		return super().form_valid(form)

class MissionDeleteView(LoginRequiredMixin, DeleteView):
	model = Mission
	success_url = "/"
	# template_name = "studens/edit.html"
	login_url = "login" # this for LoginRequiredMixin

class ProjectCreateView(LoginRequiredMixin, CreateView):
	model = Projects
	fields = ['name', 'date', 'nots' ]
	template_name = "studens/add_Project.html"
	login_url = "login" # this for LoginRequiredMixin

class StagesCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = Stages
	fields = ['name' ]
	template_name = "studens/add_Stages.html"
	login_url = "login" # this for LoginRequiredMixin

	def test_func(self):
		if self.request.user.is_staff:
			return True
		return False
		
class Job_TypeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = Job_Type
	fields = ['name', "m3_day" ]
	template_name = "studens/add_Job_Type.html"
	login_url = "login" # this for LoginRequiredMixin

	def test_func(self):
		if self.request.user.is_staff:
			return True
		return False

def TimeSheet(request,id):
	lis = []
	sta = MissionTimeSheet.objects.filter(mission__id=id)
	for i in sta:
		lis.append(list(i.employee.values_list("name","salary")))
	id_ = id 
	conv_list = list(lis)
	target_mission = Mission.objects.get(id = id)
	title = f"{target_mission.project_Name} / {target_mission.project_Stage_format} / {target_mission.project_Job_Type}"
	hours =[]
	costlist =[]
	for item in conv_list:
		cost = 0
		for i in item:
			cost+= (i[1]/30) + working_lisence_year + igama_year + insurance + electric + cars
		hours.append(len(item)*8)
		costlist.append(cost)
	hours = f"{sum(hours):.0f}"
	costlist = f"{sum(costlist):,.2f}"

	return render(request, "studens/showTimeSheet.html", {
		"Mission":sta,
		"hours": hours, 
		"costlist":costlist,
		"id_": id_,
		"title": title,
		
		})

class TimeSheetCreateView(LoginRequiredMixin, CreateView):
	model = MissionTimeSheet
	form_class = MissionTimeSheetForm
	# fields = ['date', 'mission', 'employee', 'nots' ]
	template_name = "studens/addTimeSheet.html"
	login_url = "login" # this for LoginRequiredMixin
	
	def get_initial(self):
		myid = self.kwargs['id_']
		if myid :
			return {"mission":myid}

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# user = self.request.user
		context["myid"] = self.kwargs['id_']
		return context

class TimeSheetDeleteView( DeleteView):
	model = MissionTimeSheet
	template_name = "studens/showTimeSheet.html"

	def get_success_url(self):
		post = self.object.mission 
		return reverse_lazy('showTimeSheet', kwargs={'id': post.id})

def testing(request):
	lis = []
	lisid = []
	sta = MissionTimeSheet.objects.filter(mission__id=1)
	for i in sta:
		lis.append(list(i.employee.values_list("name","salary")))
	id_ = i.mission.id 
	conv_list = list(lis)
	m2 = Mission.objects.get(id = 1)
	m = m2.project_Name
	hours =[]
	costlist =[]
	for item in conv_list:
		cost = 0
		for i in item:
			cost+= (i[1]/30) + working_lisence_year + igama_year
		hours.append(len(item)*8)
		costlist.append(cost)
	hours = sum(hours)
	costlist = sum(costlist)

	return render(request, "studens/testing.html", {
		"Mission":sta,
		"hours": hours, 
		"costlist":costlist,
		"id_": id_,
		"m": m
		})

