from django.urls import path
from .views import my_resume

urlpatterns = [
	path('', my_resume, name='my_resume'),
]