from django import forms
from .models import Projects, Mission, Stages, Job_Type, MissionTimeSheet
import datetime
from easy_select2 import select2_modelform_meta



class MissionForm(forms.ModelForm):
	Meta = select2_modelform_meta(Mission)
	# class Meta:
	# 	model = Mission
		
	# 	fields = ('project_Name', 'stages', 'project_Job_Type',
	# 	 'quantity', 'unit', 'start_Date', 'finish_Date', 'number_Of_Days',
	# 	  'number_Of_Hours',"is_mission_close" )
	# 	labels = {
	# 		"project_Name" : "اسم المشروع",
	# 		"stages" : "المرحلة المنفذة", 
	# 		"project_Job_Type" : "نوع العمل المنفذ", 
	# 		"quantity" : "الكمية", 
	# 		"unit" : "الوحدة", 
	# 		"start_Date" : "تاريخ البداية", 
	# 		"finish_Date" : "تاريخ الانتهاء", 
	# 		"number_Of_Days" : "عدد الايام", 
	# 		"number_Of_Hours" : "عدد الساعات", 	
	# 		"is_mission_close": "هل المهمة انتهت ؟"	
	# 	}
	# 	# 'field': apply_select2(forms.Select),
	# 	widgets = {
	# 		"project_Name" : forms.Select(attrs={"class": "form-control"}),
	# 		"stages" : forms.SelectMultiple(attrs={"class": "form-control"}),
	# 		"project_Job_Type" : forms.Select(attrs={"class": "form-control"}),
	# 		"quantity" : forms.NumberInput(attrs={"class": "form-control"}), 
	# 		"unit" : forms.Select(attrs={"class": "form-control"}), 
	# 		"start_Date" : forms.SelectDateWidget(attrs={"class": "form-control "},years=[datetime.date.today().year-i for i in range(5)]), 
	# 		"finish_Date" : forms.SelectDateWidget(attrs={"class": "form-control "},years=[datetime.date.today().year-i for i in range(5)]),
	# 		"number_Of_Days" : forms.NumberInput(attrs={"class": "form-control"}), 
	# 		"number_Of_Hours" : forms.NumberInput(attrs={"class": "form-control"}), 
	# 		"is_mission_close": forms.CheckboxInput(attrs={"class": "form-control"}),
	# 	}

class ProjectsForm(forms.ModelForm):
	class Meta:
		model = Projects
		fields = ("name", "date", "nots")
		labels = {
			"name" : "إسم المشروع",
			"date" : "تاريخ الاستلام", 
			"nots" : "ملاحظات"
		}

		widgets = {
			"name" : forms.TextInput(attrs={"class": "form-control"}),
			"date" : forms.SelectDateWidget(attrs={"class": "form-control "},years=[datetime.date.today().year-i for i in range(5)]),
			"nots" : forms.Textarea(attrs={"class": "form-control"})
		}

class StagesForm(forms.ModelForm):
	class Meta:
		model = Stages
		fields = ("name", )
		labels = {
			"name" : "اسم المرحلة",
		}

		widgets = {
			"name" : forms.TextInput(attrs={"class": "form-control"}),

		}

class Job_TypeForm(forms.ModelForm):
	class Meta:
		model = Job_Type
		fields = ("name", "m3_day")
		labels = {
			"name" : "اسم العمل المنفذ",
			"m3_day" : "معدل الانجاز في اليوم", 
		}

		widgets = {
			"name" : forms.TextInput(attrs={"class": "form-control"}),
			"m3_day" : forms.NumberInput(attrs={"class": "form-control"})
		}

class MissionTimeSheetForm(forms.ModelForm):
	Meta = select2_modelform_meta(MissionTimeSheet)
	# class Meta:
	# 	model = select2_modelform(MissionTimeSheet)
		
	# 	fields = ('date', 'employee','nots' )
	# 	labels = {
	# 		"date" : "التاريخ",
	# 		"employee" : "الموظفين", 
	# 		"nots" : "ملاحظات", 

	# 	}
	# 	# 'field': apply_select2(forms.Select),
	# 	widgets = {
	# 		"date" : forms.SelectDateWidget(attrs={"class": "form-control "},years=[datetime.date.today().year-i for i in range(5)]),
	# 		"employee" : forms.SelectMultiple(attrs={"class": "form-control"}),
	# 		"nots" : forms.Textarea(attrs={"class": "form-control"}),

	# 	}