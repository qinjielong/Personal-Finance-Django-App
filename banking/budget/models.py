from django.db import models
from django.utils.text import slugify

class Budget(models.Model):
    name = models.CharField(max_length=50)
    #slug 是唯一的字段，不能出现重复 slug，所以 SlugField 的属性是 unique=True
    slug = models.SlugField()

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        print(self.slug)
        super(Budget, self).save()

class MonthlyBudget(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="monthly_budget")
    month = models.DateField()
    planned = models.DecimalField(max_digits=65, decimal_places=2)
    actual = models.DecimalField(max_digits=65, decimal_places=2, blank=True, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        forslug = "{0.budget}-{0.month}".format(self)
        self.slug = slugify(forslug)
        super(MonthlyBudget, self).save()

#TO DO Add savings goals
