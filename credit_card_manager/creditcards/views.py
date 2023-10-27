from multiprocessing import context
from re import template
from django.shortcuts import render
from .models import CreditCards

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def creditcards(request):
    my_credit_cards = CreditCards.objects.all().values
    template = loader.get_template('creditcards.html')
    context = {
        'my_credit_cards': my_credit_cards,
    }
    return HttpResponse(template.render(context, request))

def card_info(request, id):
    credit_card = CreditCards.objects.get(id=id)
    template = loader.get_template('cardinfo.html')
    context = {
        'credit_card': credit_card,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
