from django import forms
from django.contrib.auth.models import User
from .models import Company
from validate_email import validate_email
# from django_countries.widgets import CountrySelectWidget

import re

class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'nip', 'country', 'city', 'street', 'zipcode', 'phone', 'email')
        # widgets = {'country': CountrySelectWidget()}


    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)

    def clean_zipcode(self):
        cd = self.cleaned_data
        code = cd.get('zipcode')
        if not re.match(r'\d{2}-\d{3}', str(code)):
            raise forms.ValidationError("Should look like this 00-000.")
        return code

    def clean_phone(self):
        cd = self.cleaned_data
        phone = cd.get('phone')
        if not re.match(r'(\+?)\d(-?\d){10}$', str(phone)):
            raise forms.ValidationError(
                "Must consist of 10 digits, '+' allowed on beginning, '-' allowed.")
        return phone

    # def checksum(number):
    #     """Calculate the checksum."""
    #     weights = (6, 5, 7, 2, 3, 4, 5, 6, 7, -1)
    #     return sum(w * int(n) for w, n in zip(weights, number)) % 11
    #
    # def clean_nip(self):
    #     cd = self.cleaned_data
    #     nip = cd.get('nip')
    #
    #     if not re.match(r'(\d){10}$', str(nip)):
    #         raise forms.ValidationError(
    #             "Must consist of 10 digits.")
    #     if checksum(nip) != 0:
    #         raise forms.ValidationError("InvalidChecksum")
    #     return nip
#
    def clean_email(self):
        cd = self.cleaned_data
        email = cd.get('email')
        if not validate_email(str(email)):
            raise forms.ValidationError("Should look like this example@example.com")
        return email

class AddUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password')


class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'is_superuser')