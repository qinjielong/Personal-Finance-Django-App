from django.contrib import admin
from .models import Budget, MonthlyBudget

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name')

class MonthlyBudgetAdmin(admin.ModelAdmin):
    list_display = ('planned', 'actual', 'slug')

admin.site.register(Budget, BudgetAdmin)
admin.site.register(MonthlyBudget, MonthlyBudgetAdmin)
