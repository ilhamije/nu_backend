# from django.contrib.postgres.fields import ArrayField
from django.db import models


class Lapak(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=280)
    picture1 = models.URLField(default="http://placekitten.com/200/200")
    picture2 = models.URLField(blank=True, null=True)
    picture3 = models.URLField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    related_url = models.CharField(max_length=200, blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    additional_info = models.ArrayField(models.CharField(max_length=300), default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey('authentication.CustomUser', related_name='listings', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']
