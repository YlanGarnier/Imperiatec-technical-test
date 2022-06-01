from django import forms
from users.models import User
from users.models import Reservation

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"