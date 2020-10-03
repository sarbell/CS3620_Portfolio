from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobbies, Portfolio


# Create your views here.

def home(request):
    return render(request, 'portfolioApp/home.html')


def hobbies(request):
    hobby_list = Hobbies.objects.all()
    context = {
        'hobby_list':hobby_list,
    }
    return render(request, 'portfolioApp/hobbies.html', context)


def portfolio(request):
    portfolio_list = Portfolio.objects.all()
    context = {
        'portfolio_list':portfolio_list,
    }
    return render(request, 'portfolioApp/portfolio.html', context)


def contact(request):
    return render(request, 'portfolioApp/contact.html')


def details(request, hobby_id):
    hobby = Hobbies.objects.get(pk=hobby_id)
    context = {
        'hobby': hobby
    }
    return render(request, 'portfolioApp/details.html', context)


def portfolio_details(request, portfolio_id):
    portfolio_item = Portfolio.objects.get(pk=portfolio_id)
    context = {
        'portfolio_item': portfolio_item
    }
    return render(request, 'portfolioApp/portfolio_details.html', context)