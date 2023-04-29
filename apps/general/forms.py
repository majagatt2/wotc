from django import forms
from apps.general.models import Volunteer


class VolunteerForm(forms.ModelForm):

    class Meta:
        model = Volunteer
        fields = [

            'activities',
            'first_name',
            'last_name',
            'email',
            'phone',

        ]

        labels = {
            
        }

        widgets = {
           

        }
