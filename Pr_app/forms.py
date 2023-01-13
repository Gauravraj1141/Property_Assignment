from django import forms

from .models import Property_detail


class Pr_form(forms.ModelForm):

    class Meta:
        model = Property_detail

        fields = ('Property_name', 'Property_address',
                  'City_name', 'State_name', )
        widgets = {"Property_name": forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Write Property Name.."}),
            "Property_address": forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Write Address .."}),
            "City_name": forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Write City Name .."}),
            "State_name": forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Write State Name .."})}
