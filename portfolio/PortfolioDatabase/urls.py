from . import views
from django.urls import path

app_name = 'portfolioApp'
urlpatterns = [
    path('', views.home, name="home"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('hobbies/<int:hobby_id>', views.details, name="details"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('add', views.create_portfolio_item, name="create_portfolio_item"),
    path('portfolio/<int:portfolio_id>', views.portfolio_details, name="portfolio_details"),
    path('edit/<int:portfolio_id>', views.edit_item, name="edit_item"),
    path('delete/<int:portfolio_id>', views.delete_item, name="delete_item"),
    path('contact/', views.contact, name="contact"),
]