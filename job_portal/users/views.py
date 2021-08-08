from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import user_passes_test


def working_check(user):
    return user.is_working

def recruiter_check(user):
    return user.is_recruiter

def login_main(request):
    return render(request,'users/login_main.html')

def signup_main(request):
    return render(request,'users/signup_main.html')

# Create your views here.
def register(request):
    uerror = ""
    werror = "" 
    if request.method=='POST':
        u_form = UserRegisterForm(request.POST)
        w_form = WorkingRegisterForm(request.POST, request.FILES)
        if u_form.is_valid() and w_form.is_valid():
            user = u_form.save()
            user.first_name = u_form.cleaned_data['first_name']
            user.last_name = u_form.cleaned_data['last_name']
            user.is_working = True
            user.save()
            uname = u_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {uname}!')
            wuser = w_form.save(commit=False)
            wuser.user=user
            wuser.save()
            return redirect('login_main')
        else:
            uerror = u_form.errors
            werror = w_form.errors
    else:
        u_form = UserRegisterForm()
        w_form = WorkingRegisterForm()
    return render(request,'users/signup.html',{'u_form':u_form,'w_form':w_form,'uerror':uerror,'werror':werror})


def recruiter_register(request):
    uerror = ""
    rerror = ""
    if request.method=='POST': 
        u_form = UserRegisterForm(request.POST)
        r_form = RecruiterRegisterForm(request.POST, request.FILES)
        if u_form.is_valid() and r_form.is_valid():
            user = u_form.save()
            user.first_name = u_form.cleaned_data['first_name']
            user.last_name = u_form.cleaned_data['last_name']
            user.is_recruiter = True
            user.save()
            uname = u_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {uname}!')
            ruser = r_form.save(commit=False)
            ruser.user=user
            ruser.save()
            return redirect('login_main')
        else:
            uerror = u_form.errors
            rerror = r_form.errors
    else:
        u_form = UserRegisterForm()
        r_form = RecruiterRegisterForm()
    return render(request,'users/recruiter_signup.html',{'u_form':u_form,'r_form':r_form,'uerror':uerror,'rerror':rerror})

def admin_register(request):
    uerror = ""
    aerror = ""
    if request.method=='POST':
        u_form = UserRegisterForm(request.POST)
        a_form = AdminRegisterForm(request.POST, request.FILES)
        if u_form.is_valid() and a_form.is_valid():
            user = u_form.save()
            user.first_name = u_form.cleaned_data['first_name']
            user.last_name = u_form.cleaned_data['last_name']
            user.is_admin = True
            user.save()
            uname = u_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {uname}!')
            auser = a_form.save(commit=False)
            auser.user=user
            auser.save()
            return redirect('login_main')
        else:
            uerror = u_form.errors
            aerror = a_form.errors
    else:
        u_form = UserRegisterForm()
        a_form = AdminRegisterForm()
    return render(request,'users/admin_signup.html',{'u_form':u_form,'a_form':a_form,'uerror':uerror,'aerror':aerror})


@login_required
def update_profile_working(request):
    if request.user.is_working:
        uerror=""
        werror=""
        if request.method == 'POST':
            u_uform = UserUpdateForm(request.POST,instance = request.user)
            w_uform = WorkingUpdateForm(request.POST, request.FILES, instance=request.user.working_user)
            if u_uform.is_valid() and w_uform.is_valid():
                u_uform.save()
                w_uform.save() 
                messages.success(request, f'profile updated !')
                return redirect('working_profile')
            else:
                uerror = u_uform.errors
                werror = w_uform.errors
                w_uform.save()
                
        else:
            u_uform = UserUpdateForm(instance = request.user)
            w_uform = WorkingUpdateForm(instance = request.user.working_user)
        return render(request,'users/profile.html',{'u_uform':u_uform,'w_uform':w_uform,'werror':werror,'uerror':uerror})
    else:
        return redirect('eh')

@login_required
def upload_newsletter(request):
    if request.user.is_admin:
        if request.method=='POST':
            n_u_form = NewsLetterUpload(request.POST, request.FILES)
            if n_u_form.is_valid():
                n_u_form.save()
                messages.success(request, f'newsletter uploaded !')
                return redirect('newsletter_view')
        else:
            n_u_form = NewsLetterUpload()
        return render(request, 'users/newsletterupload.html',{'n_u_form':n_u_form})
    else:
        return redirect('eh')
 
@login_required
def newsletterview(request):
    if request.user.is_admin:
       entries = NewsLetterModel.objects.order_by('-date_posted')
       return render(request,'users/newsletterview.html',{'entries':entries}) 
    else:
        return redirect('eh') 

@login_required
def update_profile_admin(request):
    if request.user.is_admin:
        if request.method == 'POST':
            u_uform = UserUpdateForm(request.POST,instance = request.user)
            a_uform = AdminUpdateForm(request.POST, request.FILES, instance=request.user.admin_user)
            if u_uform.is_valid() and a_uform.is_valid():
                u_uform.save()
                a_uform.save()
                messages.success(request, f'profile updated !')
                return redirect('admin_profile')
            else:
                uerror = u_uform.errors
                aerror = a_uform.errors
        else:
            u_uform = UserUpdateForm(instance = request.user)
            a_uform = AdminUpdateForm(instance = request.user.admin_user)
        return render(request,'users/profile_admin.html',{'u_uform':u_uform,'a_uform':a_uform})
    else:
        return redirect('eh')

@login_required
def update_profile_recruiter(request):
    if request.user.is_recruiter:
        if request.method == 'POST':
            u_uform = UserUpdateForm(request.POST,instance = request.user)
            r_uform = RecruiterUpdateForm(request.POST, request.FILES, instance=request.user.recruiter_user)
            if u_uform.is_valid() and r_uform.is_valid():
                u_uform.save()
                r_uform.save() 
                messages.success(request, f'profile updated !')
                return redirect('recruiter_profile')
            else: 
                uerror = u_uform.errors
                rerror = r_uform.errors
        else:
            u_uform = UserUpdateForm(instance = request.user)
            r_uform = RecruiterUpdateForm(instance = request.user.recruiter_user)
        return render(request,'users/profile_recruiter.html',{'u_uform':u_uform,'r_uform':r_uform})
    else:
        return redirect('eh')

def recruiter_login(request):
    if request.method == 'POST':
        r_lform = RecruiterLoginForm(request.POST)
        if r_lform.is_valid():
            uname = r_lform.cleaned_data.get('username')
            pwd = r_lform.cleaned_data.get('password')
            user= authenticate(username=uname, password=pwd)
            if user is not None:
                print(user.is_recruiter)
                if user.is_recruiter:
                    x = Recruiter.objects.get(user=user)
                    if x.verified:
                        login(request, user)
                        return redirect('home')
                    else:
                        return redirect('verification_wait')
                else:
                    messages.warning(request, f'You account does not have access to recruiter login since it is not a recruiter account')
                
            else:
                messages.warning(request, f'Invalid credentials please retry')
    else:
        r_lform = RecruiterLoginForm()
    return render(request, 'users/recruiter_login.html',{'r_lform':r_lform})

def verification_wait_view(request):
    return render(request, 'users/verification_wait.html')

def admin_login(request):
    if request.method == 'POST':
        a_lform = AdminLoginForm(request.POST)
        if a_lform.is_valid():
            uname = a_lform.cleaned_data.get('username')
            pwd = a_lform.cleaned_data.get('password')
            user= authenticate(username=uname, password=pwd)
            if user is not None: 
                if user.is_admin:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.warning(request, f'You account does not have access to Admin login since it is a basic_user account')
            else:
                messages.warning(request, f'Invalid credentials please retry')
    else:
        a_lform = AdminLoginForm()
    return render(request, 'users/admin_login.html',{'a_lform':a_lform})


@login_required
def change_status(request,pk):
    r = Recruiter.objects.get(id=pk)
    if request.user.is_admin:
        if r.verified:
            r.verified = False
            r.save()
            return redirect('recruiter_request')
        else:
            r.verified = True
            r.save()
            return redirect('recruiter_request')
    else:
        return redirect('eh') 

def eh_view(request):
    return render(request,'users/eh.html')

@login_required
def recruiter_request_view(request):
    if request.user.is_admin:
        recruiters = Recruiter.objects.all()
        return render(request,'users/recruiter_request.html',{'recruiters':recruiters})
    else:
        return redirect('eh')