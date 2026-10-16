from django.urls import path
from. import views

urlpatterns = [
    path('', views.home, name='home'),
    path('find-jobs/', views.find_jobs, name='find_jobs'),
    path('companies/', views.companies, name='companies'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('job/<int:job_id>/apply/', views.apply_job, name='apply_job'),
    path('about/', views.about, name='about'),
    path('login/', views.login_page, name='login'),
]