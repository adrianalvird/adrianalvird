from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,'index.html')
 
def about(request):
	return render(request,'about.html')
	
def resume(request):
	return render(request,'resume.html')
	
def skills(request):
	return render(request,'skills.html')
	


	



