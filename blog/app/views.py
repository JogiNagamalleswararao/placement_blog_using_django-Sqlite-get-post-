from django.shortcuts import render
from django.http import HttpResponse
from .models import Job,feedback

def app(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        area=request.POST['area']
        print(name,email)
        obj=feedback()
        obj.name=name
        obj.email=email
        obj.area=area
        obj.save()
        return render(request,"feedback.html")
    post1=Job.objects.all()
    return render(request,"index.html",{'post1':post1})
# Create your views here.
