from django import forms


class AddressForm(forms.Form):
    address = forms.CharField()
    city = forms.CharField()
    radius = forms.IntegerField()