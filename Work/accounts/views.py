from django.shortcuts import render 
from .forms import  CustomUserCreationForm , ContactForm
from django.urls import reverse_lazy
from django.views.generic import CreateView , FormView
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail

# Create your views here.
class SignUpView(CreateView):
    form_class =  CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')



class ContactView(CreateView):
    template_name = 'registration/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

