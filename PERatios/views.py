from django.shortcuts import render, redirect
from .models import PE_Data
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'variable_name': 'Hello, Django!',
        'another_variable': 123
    }
    # The render function takes the request, the template name, and an optional dictionary (context)
    return render(request, 'peratios.html', context)