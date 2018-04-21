from django.db import models
from django.contrib.auth.models import User
import datetime


class Product(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    text = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def pub_date(self):
        return self.date.strftime('%b %e %Y')

    def summary(self):
        return "{}{}".format(self.text[:100], '...')
