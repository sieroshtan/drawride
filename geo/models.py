from django.db import models
from django.core.urlresolvers import reverse


class Country(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)


class City(models.Model):
    country = models.ForeignKey(Country, related_name='cities')
    name = models.CharField(max_length=255)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('city', args=(self.id,))
