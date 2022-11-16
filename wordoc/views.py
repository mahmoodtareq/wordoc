import re
from django.shortcuts import render
from django.http import HttpResponse
from wordoc.data import get_words, exists
import random

def index(request):
    words = get_words()
    word = random.choice(words)
    return render(request, 'index.html', {'word': word})


def check(request):
    guess = request.GET.get('word')
    guess = guess.strip().upper()
    if exists(guess):
        return HttpResponse('true')
    else:
        return HttpResponse('false')
