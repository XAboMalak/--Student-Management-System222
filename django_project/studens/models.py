from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse



#######################################################
year = 360
working_hours = 8
working_lisence_year = 9700/year # تكلفة رخصة العمل في السنة
igama_year = 650/year #تكلفة الاقامة في السنة
insurance = 1000/year # تكلفة التأمين الطبي + التامينات الاجتماعية علي العامل في السنة
electric = 650/year #تكلفة الكهرباء في السنة علي العامل 
cars = 1 #تكلفة ترحيل العامل الواحد في اليوم بالريال
#######################################################
class Projects(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="إسم المشروع")
    date = models.DateField(default=date.today, verbose_name="تاريخ الاستلام")
    nots = models.TextField(null=True, blank=True, verbose_name="ملاحظات")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("add")

class Stages(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="إسم المرحلة")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("add")

class Job_Type(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="إسم نوع العمل")
    m3_day = models.FloatField(verbose_name="كمية الانجاز في اليوم" )

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("add")

class Mission(models.Model):
    unit_choice = (('1', 'متر مكعب'), ('2', 'طابوقة'),('3', 'متر مربع'), ('4', 'متر طولي'),)
    project_Name = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name="إسم المشروع")
    stages = models.ManyToManyField(Stages, verbose_name="المرحلة")
    project_Job_Type = models.ForeignKey(Job_Type, on_delete=models.CASCADE, verbose_name="نوع العمل")
    quantity = models.IntegerField( verbose_name="الكمية")
    unit = models.CharField(max_length=1, choices=unit_choice, verbose_name="الوحدة")
    start_Date = models.DateField(default=date.today, verbose_name="تاريخ البداية")
    finish_Date = models.DateField(default=date.today, verbose_name="تاريخ الانتهاء")
    number_Of_Days = models.IntegerField( verbose_name="عدد الايام")
    number_Of_Hours = models.IntegerField( verbose_name="عدد الساعات")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="الإنشاء بواسطة")
    updated_by = models.CharField(max_length=100, null=True, blank=True, verbose_name="التعديل بواسطة")
    is_mission_close = models.BooleanField(default=False, verbose_name="انتهت المهمة ؟")

    def __str__(self) -> str:
        return f"{self.project_Job_Type} {self.project_Name}"

    @property
    def created_format(self):
        c_at = self.created_at.strftime("%Y/%m/%d")
        c_by = self.created_by
        return f"Created By {c_by} @ {c_at}"

    def update_format(self):
        u_at = self.updated_at.strftime("%Y/%m/%d")
        u_by = self.updated_by
        if u_by:
            return f"Updated By {u_by} @ {u_at}"
        return " "

    def get_absolute_url(self):
        return reverse("index")

    @property
    def production_Ratio(self):
        Hours = self.number_Of_Hours
        Q = self.quantity
        M3 = self.project_Job_Type.m3_day
        try:
            P_Ratio = (Q/(M3/2)*(8/Hours))*100
            return f"{P_Ratio:.0f} %"
        except:
            return 0
        
    @property
    def project_Stage_format(self):
        title =[]
        txt = ""
        for i, x in enumerate(self.stages.all()):
            title.append(x)
            txt = txt + " " + str(title[i])
        return txt

class Jobs(models.Model):
    job_name = models.CharField(max_length=100, unique=True, verbose_name="إسم الوظيفة")
    def __str__(self):
        return self.job_name
    
class Employee(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="إسم الموظف")
    job_name = models.ForeignKey(Jobs, on_delete=models.CASCADE, verbose_name="إسم الوظيفة")
    salary = models.IntegerField(verbose_name="الراتب")
    def __str__(self):
        return self.name

class MissionTimeSheet(models.Model):
    date = models.DateField(default=date.today, verbose_name="التاريخ")
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, verbose_name="إسم المهمة")
    employee = models.ManyToManyField(Employee, verbose_name="إسم الموظفين")
    nots = models.TextField(null=True, blank=True, verbose_name="ملاحظات")

    def get_absolute_url(self): 
        return reverse("showTimeSheet",kwargs={'id':self.mission_id})
    
    def __str__(self) -> str:
        return f"{self.date} - {self.mission}"

    @property
    def employee_format(self):
        txt = ""
        for  x in self.employee.all().values_list("name"):
            txt = txt + " | " + str(x[0])
        return txt

    @property
    def employee_count(self):
        x = self.employee.all().values_list("name")   
        tottal_hours = len(x) * working_hours
        return tottal_hours

    @property
    def employee_cost(self):
        employeeName =[]
        cost_employe = 0
        for employee in self.employee.all().values_list("name","salary"):
            cost_employe+= (employee[1]/30) + working_lisence_year + igama_year + insurance + electric + cars
        return f"{cost_employe:.2f}"
