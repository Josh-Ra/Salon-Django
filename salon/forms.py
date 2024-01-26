from django import forms
from .models import stylist, Bookings


class StylistRegisterForm(forms.ModelForm):
    class Meta:
        model = stylist
        fields = ["name", "image", "description"]

    def __str__(self):
        return self.name


class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ["date", "time", "service"]
        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date"}
            ),
            "time": forms.TimeInput(
                attrs={"type": "time"}
            ),
        }

    def __str__(self):
        return self.name


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    description = forms.CharField()
