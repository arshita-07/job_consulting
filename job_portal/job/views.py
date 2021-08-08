from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from job.models import *
from django.http import HttpResponse
from django import forms
from .forms import *
from django.contrib.auth.decorators import login_required
from job_portal.settings import EMAIL_HOST_USER, BASE_DIR
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMessage
from users.models import *


# Create your views here.

def home(request):
    if request.method=='POST':
        n_form = NewsLetter(request.POST)
        if n_form.is_valid():
            recepient = n_form.cleaned_data.get('email')
            subject = "Newsletter from Implicit Consulting inc."
            message = "Greetings from Implicit Consulting inc!!"
            email = EmailMessage(subject, message, EMAIL_HOST_USER, [recepient])
            file = NewsLetterModel.objects.order_by('-date_posted')[0]
            z=file.newsletter.url
            z=z[1:]
            print(z)
            email.attach_file(z)
            email.send(fail_silently=False)
            messages.success(request, 'Our newsletter has been sent to the email address entered by you')
    else:
        n_form = NewsLetter()
    return render(request,'job/home.html',{'n_form':n_form})

def done(request):
    return render(request,'job/done.html')

@login_required
def apply(request, pk):
    job = Job.objects.get(pk=pk)
    user = request.user
    if Application.objects.filter(job=job, applicant=user.working_user):
        return redirect('done')
    else:
        if user.is_working:
            if request.method == 'POST':
                application_form = CV(request.POST , request.FILES)
                if application_form.is_valid():
                    application = application_form.save(commit=False)
                    application.applicant = user.working_user
                    application.job = job
                    application.save()
                    job.applicants.add(user.working_user)
                    job.save()
                    return redirect('myapplications')
            else:
                application_form = CV()
        else:
            return redirect('eh')
        return render(request,'job/apply.html',{'job':job,'user':user,'form':application_form})

@login_required
def myapplications(request):
    user = request.user
    if user.is_working:
        applications=Application.objects.filter(applicant=user.working_user)
        return render(request,'job/applications.html',{'applications':applications})
    else:
        return redirect("eh")

@login_required
def applicationforjob(request,pk):
    if request.user.is_recruiter:
        job = Job.objects.get(pk=pk)
        applications = Application.objects.filter(job = job)
        return render(request,'job/afj.html',{'applications':applications,'job':job})
    else:
        return redirect('eh')
    

class JobListView(ListView):
    model = Job
    template_name = 'job/job_list.html'
    context_object_name ='jobs'
    ordering = ['-date_posted']

class JobDetailView(DetailView):
    model = Job
    context_object_name ='job'
    template_name = 'job/job_detail.html'

class JobUpdateView(UserPassesTestMixin ,LoginRequiredMixin, UpdateView):
    model = Job
    fields = ['title','job_description','required_skills','apply_deadline','keywords','status']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['apply_deadline'].widget = forms.DateInput(attrs={'type':'date'})
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.recruiter.user:
            return True
        else:
            return False

class JobCreateView(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Job
    fields = ['title','job_description','required_skills','apply_deadline','keywords','status','location','work_from_home']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['apply_deadline'].widget = forms.DateInput(attrs={'type':'date'})
        return form

    def form_valid(self, form):
        form.instance.recruiter = self.request.user.recruiter_user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_recruiter:
            return True
        else:
            return False

class JobDeleteView(UserPassesTestMixin ,LoginRequiredMixin, DeleteView):
    model = Job
    success_url = '/job/job_list'

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.recruiter.user:
            return True
        else:
            return False
