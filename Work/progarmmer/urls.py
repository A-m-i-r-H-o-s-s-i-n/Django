from django.urls import path ,re_path
from django.conf import settings
from .views import HomeView , ResumeView , ProjectView , Newresume , Newproject

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('resumes/', ResumeView.as_view(), name='resume'),
    path('projects/', ProjectView.as_view(), name='project'),
    path('resume/new', Newresume.as_view(), name='new_resume'),   
    path('project/new', Newproject.as_view(), name='new_project'),
]