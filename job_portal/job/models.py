from django.db import models
from users.models import *
from django.utils import timezone
from django.urls import reverse
from datetime import date
 
# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length = 300, null = False )
    recruiter = models.ForeignKey(Recruiter,on_delete=models.CASCADE, related_name="recruiter")
    job_description = models.TextField(null = False)
    date_posted = models.DateTimeField(default = timezone.now)
    keywords = models.CharField(max_length = 200,null=False, default='NA')
    applicants = models.ManyToManyField(WorkingUser,through='Application',related_name = "applicants")
    status = models.BooleanField(default=False)
    required_skills = models.TextField(null=False)
    apply_deadline = models.DateField(verbose_name='Apply by',null=True)
    location = models.CharField(max_length=300, null=False, default='work from home only')
    work_from_home = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})

    @property
    def is_past_due(self):
        return date.today() > self.apply_deadline
 

class Application(models.Model):
    applicant = models.ForeignKey(WorkingUser,on_delete=models.CASCADE, related_name="applicant")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job')
    cv = models.FileField(upload_to='cv')
    

    