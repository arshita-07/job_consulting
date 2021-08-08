from django.contrib import admin
from django.urls import path
from job import views
from .views import *

urlpatterns = [
    path('home/', views.home, name="home"),
    path('done/', views.done, name="done"),
    path('job_list/', JobListView.as_view(), name="list"),
    path('detail/<int:pk>/',JobDetailView.as_view(),name='detail'),
    path('update/<int:pk>/',JobUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',JobDeleteView.as_view(),name='delete'),
    path('create/',JobCreateView.as_view(),name='create'),
    path('apply/<int:pk>/', views.apply, name="apply"), 
    path('myapplications/',views.myapplications, name="myapplications"),
    path('applicationforjob/<int:pk>',views.applicationforjob,name ="applicationforjob")
]