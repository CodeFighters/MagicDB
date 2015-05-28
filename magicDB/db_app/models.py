from django.db import models
from django.core.urlresolvers import reverse

class Lists(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return "/list/{}/".format(self.name)
        return reverse('list', args=[str(self.name)])

class Groceries(models.Model):
    name = models.CharField(max_length=100)
    list_name = models.ForeignKey(Lists)
    quantity = models.SmallIntegerField()
    measurement = models.CharField(max_length=20)
    is_bought = models.BooleanField()

    def __str__(self):
        return "{} {} {}".format(self.name, self.quantity, self.measurement)
