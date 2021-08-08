from django.contrib import admin
from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login_main',user_views.login_main, name = "login_main"),
    path('signup_main',user_views.signup_main, name = "signup_main"),
    path('user_signup/', user_views.register, name="user_signup"),
    path('user_login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="user_login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('working_profile/', user_views.update_profile_working, name="working_profile"),
    path('admin_profile/', user_views.update_profile_admin, name="admin_profile"),
    path('recruiter_profile/', user_views.update_profile_recruiter, name="recruiter_profile"),
    path('recruiter_login/', user_views.recruiter_login, name="recruiter_login"),
    path('recruiter_signup/', user_views.recruiter_register, name="recruiter_signup"),
    path('admin_login/', user_views.admin_login, name="admin_login"),
    path('admin_signup/', user_views.admin_register, name="admin_signup"),
    path("eh/",user_views.eh_view,name='eh'),
    path("recruiter_request/",user_views.recruiter_request_view,name='recruiter_request'),
    path('change_status/<int:pk>/',user_views.change_status, name='change_status'),
    path('verification_pending/',user_views.verification_wait_view, name = 'verification_wait'),
    path('newsletterupload/',user_views.upload_newsletter, name = 'newsletterupload'),
    path('newsletterview/',user_views.newsletterview, name = 'newsletter_view'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name="password_reset"),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name="password_reset_confirm"),
 

]
