from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Sum
from course_planner.models import Course, Requirement, Quarter

def calendar(request):
    years = Quarter.objects.values('year').annotate(quarters=Count('season')).order_by()
    quarters = Quarter.objects.annotate(units=Sum('course__units'))
    req_sources = Requirement.objects.values('source').annotate(reqs=Count('id')).order_by()
    requirements = Requirement.objects.all()
    for r in requirements:
        r.quarters = Quarter.objects.all()
        for q in r.quarters:
            q.courses = q.course_set.filter(requirements=r)

    return render(request, "course_planner/calendar.html", {
        "years": years,
        "quarters": quarters,
        "req_sources": req_sources,
        "requirements": requirements
    })

def requirements(request):
    requirements = Requirement.objects.all()
    return render(request, "course_planner/requirements.html", {
        "requirements": requirements
    })
    
