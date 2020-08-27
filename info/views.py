from django.shortcuts import render
from django.views.generic import TemplateView
from info.models import Quote
from django.http import JsonResponse
import random
facts = []
for i in Quote.objects.all():
    facts.append(i.text)


def home(request):
    """return a random quote from Quote.objects.all()"""
            
    return JsonResponse({'fact-sphere-quote':random.choice(facts)})
