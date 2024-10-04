from django.shortcuts import render, redirect, get_object_or_404
from django.http import  HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from App.models import *


def loginPage(req):
    if req.method == "POST":
        username = req.POST.get('uname')
        password = req.POST.get('pass')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(req, user)
            messages.success(req,  'Login Successful')
            return redirect('home')
        else: 
            messages.warning(req,  'Invalid Credentials')
            return render(req, 'login.html')
    return render(req, "login.html")

def register(req):
    if req.method == 'POST':
        username = req.POST.get('uname')
        email = req.POST.get('email')
        user_type = req.POST.get('user_type')
        password = req.POST.get('pass')
        con_pass = req.POST.get('con_pass')
        if password != con_pass:
            messages.warning(req, 'Password and Confirm Password do not match')
            return render(req, 'register.html')
        else: 
            user = CustomUser.objects.create_user(username=username, email=email, user_type=user_type, password=con_pass)
            messages.success(req,  'User Created Successfully')
            return redirect('loginPage')
    return render(req, "register.html")

@login_required
def home(req):
    data = JobModel.objects.all()
    context = {
        'data': data
    }
    return render(req, "index.html", context)

@login_required
def logoutUser(req):
    logout(req)
    return redirect('loginPage')


@login_required
def addJob(req):
    if req.user.user_type == "admin":
        current_user = req.user
        if req.method == "POST":
            job_title = req.POST.get('jobTitle')
            job_description = req.POST.get('description')
            job_location = req.POST.get('location')
            salary = req.POST.get('salary')
            company_name = req.POST.get('companyName')
            emp_type = req.POST.get('employmentType')
            app_dead_line = req.POST.get('applicationDeadline')
            
            job_add = JobModel(
                user = current_user,
                job_title=job_title,
                description=job_description,
                location=job_location,
                salary=salary,
                company_name=company_name,
                employment_type=emp_type,
                application_deadline=app_dead_line
                
            )
            
            job_add.save()
            messages.success(req, 'job Added Successful')
            return redirect('home')
    return render(req, 'add_job.html')

@login_required
def applyNow(req, id):
    current_user = req.user
    current_job =  JobModel.objects.get(id=id)
    already_apply = ApplyNowModel.objects.filter(user=current_user, job=id)

    try:
        data =  get_object_or_404(JobModel, id=id)
    except Http404:
        messages.error(req, "there is something wrong")
        return redirect('home')
    
    if req.method == "POST":
        if already_apply.exists():
            messages.error(req, "you have already applied for this job")    
            
        else: 
            applicant_name = req.POST.get('fullName')
            applicant_email = req.POST.get('email')
            applicant_cv = req.FILES.get('resume')
            cover_letter = req.POST.get('coverLetter')
            
            applicant_create = ApplyNowModel(
                user = current_user,
                job = current_job,
                applicant_name=applicant_name,
                applicant_email=applicant_email,
                applicant_cv=applicant_cv,
                applicant_cover_letter=cover_letter,
                
            )
            
            applicant_create.save()
            messages.success(req, 'Application Sent Successful')

            return redirect('home')

    context = {
        'data': data,
        'already_apply':already_apply

    }
    
    return render(req,  'applyNow.html', context)


def searchJob(req):
    query = req.GET.get('search')
    if query: 
        job = JobModel.objects.filter(Q(job_title__icontains = query)|Q(description__icontains = query)|Q(location__icontains = query)|Q(company_name__icontains=query))
        
    else:
        job = JobModel.objects.none()
        
    context = {
        'job':job,
        'query':query
    } 
    
    return render(req, 'searchJob.html', context)       

    

def profile(req):
    return render(req, 'profile.html')


def createdJobsByAdmin(req):
    if req.user.user_type == 'admin':
        current_user =  req.user
        job = JobModel.objects.filter(user=current_user)
        
        context = {
            'job':job
        }
    return render(req, "createdJobByAdmin.html", context)       
            
        
def jobDelete(req,id):
    data=JobModel.objects.get(id=id)
    data.delete()
    return redirect('createdJobsByAdmin')
        

    
    
def jobEdit(req, id):
    if req.user.user_type == "admin":
        current_user = req.user
        job = JobModel.objects.get(id=id)
        if req.method == "POST":
            job_title = req.POST.get('jobTitle')
            id = req.POST.get('job_id')
            job_description = req.POST.get('description')
            job_location = req.POST.get('location')
            salary = req.POST.get('salary')
            company_name = req.POST.get('companyName')
            emp_type = req.POST.get('employmentType')
            app_dead_line = req.POST.get('applicationDeadline')
            
            job_add = JobModel(
                user = current_user,
                id = id,
                job_title=job_title,
                description=job_description,
                location=job_location,
                salary=salary,
                company_name=company_name,
                employment_type=emp_type,
                application_deadline=app_dead_line
                
            )
            
            job_add.save()
            messages.success(req, 'job Update Successful')
            return redirect('createdJobsByAdmin')
        
        
        context ={
            'job':job,
            'user':current_user
        }
        
    return render(req, "edit_job.html", context)
    
    






    





