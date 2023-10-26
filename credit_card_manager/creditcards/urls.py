from django.urls import path
from . import views

urlpatterns = [
    path('creditcards/', views.creditcards, name='creditcards'),
    path('creditcards/cardinfo/<int:id>', views.card_info, name='card information')
]