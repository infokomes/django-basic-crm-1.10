from django.db import models
from django_countries.fields import CountryField
from .const.country import *
from django.utils.translation import ugettext as _


class Company(models.Model):

    name = models.CharField(max_length=100, verbose_name=_("Name"), blank=True, null=True)
    nip = models.CharField(max_length=10, verbose_name = _("NIP") , blank=True, null=True)
    # country = models.CharField(max_length=2, choices=[(x[0], x[3]) for x in COUNTRIES], verbose_name=_("Country"), blank=True, null=True)
    country = CountryField(blank_label='(select country)')
    city = models.CharField(max_length=100, verbose_name=_("City"), blank=True, null=True)
    street = models.CharField(max_length=200, verbose_name=_("Street"), blank=True, null=True)
    zipcode = models.IntegerField(verbose_name=_("Zipcode"), blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name = _("Phone Number") , blank=True, null=True)
    email = models.EmailField(max_length=200, verbose_name = _("Email Address"), blank=True, null=True)

    def __str__(self):
        return self.name


