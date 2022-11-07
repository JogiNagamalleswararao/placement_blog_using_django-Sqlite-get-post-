from django.shortcuts import render
from django.http import HttpResponse
from .models import Job,Det

def app(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        area=request.POST['area']
        print(name,email)
        obj=Det()
        obj.name=name
        obj.email=email
        obj.area=area
        obj.save()
        return render(request,"index1.html")
    post1=Job.objects.all()
    return render(request,"base.html",{'post1':post1})
# Create your views here.
