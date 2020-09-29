from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobbies, Portfolio


# Create your views here.

def home(request):
    return HttpResponse('<h1>Welcome to Sarah Bell\'s Portfolio Site! </h1> <p>I am a student at Weber State University studying Web Devleopment. I also have an internship with Larry H Miller in web development. I am an avid runner, a lover of great food, and love to learn new things.</p>')


def hobbies(request):
    hobby_list = Hobbies.objects.all()
    return HttpResponse(hobby_list)


def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    return HttpResponse(portfolio_list)


def contact(request):
    return HttpResponse('<p>Contact Me: <strong>sarahbell@mail.weber.edu</strong></p>')