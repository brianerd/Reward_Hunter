from json.tool import main
from django.urls import path
from . import views

urlpatterns = [
    path('creditcards/', views.creditcards, name='creditcards'),
    path('creditcards/information/<int:id>', views.card_info, name='card information'),
    path('', views.main, name='main page')
]