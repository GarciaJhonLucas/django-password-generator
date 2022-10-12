from ast import For
from itertools import chain
from django.shortcuts import render
from django.http import HttpResponse, response
import random


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def password(request):
    generate_password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length_pass = int(request.GET.get('length'))
    text  = request.GET.get('especial')

    if len(text) != 0:
        characters.extend(text)
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('characters'):
        characters.extend(list('!"#$%&()*+,_./:;=<>][}@{¢£'))

    for x in range(length_pass):
        generate_password += random.choice(characters)
    
    return render(request, 'password.html', {'password':generate_password[0:length_pass]})
