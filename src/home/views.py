from django.http import HttpResponse
from django.shortcuts import render
from visits.models import pageVisit

def homePage(request,*args,**kwargs):
    qs = pageVisit.objects.all()
    page_qs = pageVisit.objects.filter(path=request.path)
    my_title = 'Home Page'
    my_context = {
        "page_title":my_title,
        "page_visit_count":page_qs.count(),
        "percent":(page_qs.count()*100)/qs.count(),
        "total_visit_count":qs.count(),
    }
    html_template = 'home.html'
    pageVisit.objects.create(path=request.path)
    return render(request,html_template,my_context)