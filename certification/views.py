from django.shortcuts import render, HttpResponse
from .models import Certification


# Create your views here.

def certification(request):

    certs = Certification.objects.all()
    
    return render(request,'certification.html', {'certs': certs})
 
