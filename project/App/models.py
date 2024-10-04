from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER=[
        ('admin', 'Admin'),
        ('viewer', 'Viewer'),
        
    ]
    
    user_type =  models.CharField(max_length=50, choices=USER, null=True)
    
    def __str__(self):
        return f"{self.username} - {self.user_type}"
    
class JobModel(models.Model):
    JOB_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
        ('temporary', 'Temporary'),

    ]    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    job_title = models.CharField(max_length=50,  null=True)
    company_name = models.CharField(max_length=50,  null=True)
    location = models.CharField(max_length=50, null=True)
    description =  models.TextField(null=True)
    salary = models.CharField(max_length=50, null=True)
    employment_type = models.CharField(choices=JOB_CHOICES, max_length=50, null=True)
    post_date  = models.DateField(auto_now_add=True, null=True)
    update_date = models.DateField(auto_now=True, null=True)
    application_deadline = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.job_title} - {self.employment_type}"
    
    
class ApplyNowModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    job =  models.ForeignKey(JobModel, on_delete=models.CASCADE, null=True)
    applicant_name = models.CharField(max_length=50, null=True)
    applicant_email = models.EmailField(max_length=100, null=True)
    applicant_cv =  models.FileField(upload_to='cv/', null=True)
    applicant_cover_letter = models.TextField(null=True)
    class meta: 
        unique_together = ['user', 'job']
    
    def __str__(self):
        return f"{self.user.username} - {self.job.job_title} - {self.applicant_email}"


    
    
    
        






