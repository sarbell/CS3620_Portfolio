from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hobbies, Portfolio, Contact
from .forms import ContactForm, PortfolioForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



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


@login_required()
def create_portfolio_item(request):
    form = PortfolioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('portfolioApp:portfolio')

    return render(request, 'portfolioApp/portfolio-form.html', {'form': form})



def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('portfolioApp:home')

    return render(request, 'portfolioApp/contact.html', {'form': form})


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


@login_required()
def edit_item(request, portfolio_id):
    portfolio_item = Portfolio.objects.get(pk=portfolio_id)
    form = PortfolioForm(request.POST or None, instance=portfolio_item)

    if form.is_valid():
        form.save()
        return redirect('portfolioApp:portfolio')

    return render(request, 'portfolioApp/portfolio-form.html', {'form': form, 'portfolio_item':portfolio_item})


@login_required()
def delete_item(request, portfolio_id):
    portfolio_item = Portfolio.objects.get(pk=portfolio_id)

    if request.method == 'POST':
        portfolio_item.delete()
        return redirect('portfolioApp:portfolio')

    return render(request, 'portfolioApp/delete_item.html', {'portfolio_item':portfolio_item})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! Your are logged in!')
            return redirect('portfolioApp:home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
