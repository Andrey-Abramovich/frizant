from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Order


class OrderForm(forms.ModelForm):
    # phone_number = PhoneNumberField(required=True)
    class Meta:
        model = Order
        fields = ('name', 'phone')
