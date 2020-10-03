from . import views
from django.urls import path

app_name = 'portfolioApp'
urlpatterns = [
    path('', views.home, name="home"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('hobbies/<int:hobby_id>', views.details, name="details"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio/<int:portfolio_id>', views.portfolio_details, name="portfolio_details"),
    path('contact/', views.contact, name="contact"),
]