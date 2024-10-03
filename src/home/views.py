from django.http import HttpResponse
from django.shortcuts import render
from visits.models import pageVisit

def homePage(request,*args,**kwargs):
    return about_view(request,*args,**kwargs)

def about_view(request,*args,**kwargs):
    qs = pageVisit.objects.all()
    page_qs = pageVisit.objects.filter(path=request.path)
    try:
        percent = (page_qs.count()*100)/qs.count()
    except:
        percent= 0
    my_title = 'Home Page'
    my_context = {
        "page_title":my_title,
        "page_visit_count":page_qs.count(),
        "percent":percent,
        "total_visit_count":qs.count(),
    }
    html_template = 'home.html'
    pageVisit.objects.create(path=request.path)
    return render(request,html_template,my_context)