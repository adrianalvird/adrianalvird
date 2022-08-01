from django.shortcuts import render, HttpResponse
from .models import Contact
# from django.urls import Path , include
from .import models

from .forms import UploadFileForm

# Create your views here.

def contact(request):
    if request.method=='POST':
   	 name = request.POST['name']
   	 priemail = request.POST['priemail']
   	 extemail = request.POST['extemail']
   	 jobdesc = request.POST['jobdesc']
   	 phone = request.POST['phone']
   	 address = request.POST['address']
   	 message = request.POST['message']
   	 
   	 contact = Contact(name=name, priemail=priemail, extemail=extemail, jobdesc=jobdesc, phone=phone, address=address, message=message)
   	 contact.save()

    return render(request,'contact.html')
 
