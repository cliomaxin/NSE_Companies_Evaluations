from django.contrib import admin
from .models import *

class PE_DataAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'current_share_price', 'earnings_per_share')
    search_fields = ('company_name',)
admin.site.register(PE_Data, PE_DataAdmin)

# admin.site.register(Company_Data)