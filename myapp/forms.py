from django.forms import ModelForm
from .models import booking,subscriber,cleaner,contact


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = booking
        fields = "__all__"

class RegistrationForm(ModelForm):
    class Meta:
        model = subscriber
        fields = "__all__"

class CleanersForm(ModelForm):
    class Meta:
        model = cleaner
        fields = "__all__"
class Contactform(ModelForm):
    class Meta:
        model = contact
        fields = "__all__"