from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from django.db.models import Q, Count

def home(request):
    latest_jobs = Job.objects.all().order_by('-id')[:3]
    return render(request, 'jobs/home.html', {'jobs': latest_jobs})

def find_jobs(request):
    query = request.GET.get('q', '')
    jobs = Job.objects.all().order_by('-id')
    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(company_name__icontains=query) |
            Q(location__icontains=query) |
            Q(description__icontains=query)
        )
    return render(request, 'jobs/find_jobs.html', {'jobs': jobs, 'query': query})

def companies(request):
    # company_name se group by
    data = Job.objects.values('company_name').annotate(total=Count('id')).order_by('-total')
    companies_list = [{'company': d['company_name'], 'total': d['total']} for d in data if d['company_name']]
    return render(request, 'jobs/companies.html', {'companies': companies_list})

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/apply.html', {'job': job})

def about(request):
    return render(request, 'jobs/about.html')

def login_page(request):
    return render(request, 'jobs/login.html')