from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'slug')

admin.site.register(Account, AccountAdmin)
