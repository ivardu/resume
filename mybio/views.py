from django.shortcuts import render

# Create your views here.


def my_resume(request):
	return render(request, 'mybio/resume.html')