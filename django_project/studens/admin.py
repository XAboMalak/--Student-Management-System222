from django.contrib import admin
from . models import (Projects, Mission, Stages, Job_Type,
 Employee, MissionTimeSheet, Jobs)
from django.db import models
from django.contrib.auth.models import User
from easy_select2 import select2_modelform


myModels =[Projects, Stages, Job_Type, Employee,
  Jobs]


MissionTimeSheetForm = select2_modelform(MissionTimeSheet )
MissionForm = select2_modelform(Mission)

class MissionTimeSheetAdmin(admin.ModelAdmin):
    form = MissionTimeSheetForm

class MissionAdmin(admin.ModelAdmin):
    form = MissionForm


admin.site.register(myModels)
admin.site.register(MissionTimeSheet,MissionTimeSheetAdmin)
admin.site.register(Mission,MissionAdmin)