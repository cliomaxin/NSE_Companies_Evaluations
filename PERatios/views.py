from django.shortcuts import render, redirect
from .models import PE_Data
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    pe_data = PE_Data.objects.all()
    
    # Calculate PE Ratio for each company
    data_with_ratio = []
    for item in pe_data:
        if item.earnings_per_share and item.earnings_per_share > 0:
            pe_ratio = round(item.current_share_price / item.earnings_per_share, 2)
        else:
            pe_ratio = 0
        
        data_with_ratio.append({
            'company_name': item.company_name,
            'current_share_price': item.current_share_price,
            'earnings_per_share': item.earnings_per_share,
            'pe_ratio': pe_ratio
        })
    
    context = {
        'pe_data': data_with_ratio,
    }
    # The render function takes the request, the template name, and an optional dictionary (context)
    return render(request, 'peratios.html', context)