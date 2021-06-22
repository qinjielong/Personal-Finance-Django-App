from django.db import models
from django.utils.text import slugify
from polymorphic.models import PolymorphicModel
import datetime

from accounts.models import Account
from budget.models import MonthlyBudget, Budget


class Category(models.Model):
    name = models.CharField(max_length=50)
    budget = models.ForeignKey(Budget, on_delete=models.DO_NOTHING, related_name="category_budget", null=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save()

    def __str__(self):
        return self.slug


class Transaction(models.Model):
    date = models.DateField()
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="trans_account")
    amount = models.DecimalField(max_digits=65, decimal_places=2)
    balance = models.DecimalField(max_digits=65, decimal_places=2)
    beneficiary = models.CharField(max_length=50)
    budget = models.ForeignKey(MonthlyBudget, blank=True, null=True, on_delete=models.DO_NOTHING, related_name="trans_monthly_budget")
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.DO_NOTHING, related_name="trans_category")
    debit = models.BooleanField(default=True)
    transfer = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        time = datetime.datetime.now().time().strftime("%H%M%S") 
        #Add the hour, min, and second to the slug to avoid Unique constraint conflicts
        forslug = "{0.date}-{1}-{0.account}-{0.amount}".format(self, time)
        self.slug = slugify(forslug)
        super(Transaction, self).save()


