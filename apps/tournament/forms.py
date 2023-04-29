from django.contrib.auth.models import User
from django.forms.fields import DateField
#from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms
from betterforms.multiform import MultiModelForm
from django.contrib.auth.forms import UserCreationForm
from apps.users.models import Person, FamilyMemberRelationship
from apps.tournament.models import Registration


class PersonForm(forms.ModelForm):
    birthdate = DateField(label='Date of Birth',
                          widget=forms.widgets.DateInput(attrs={'type': 'date', }))
    email = forms.EmailField(label='Email adress', required=True)
    

    class Meta:
        model = Person
        fields = [

            'first_name',
            'last_name',
            'phone',
            'email',
            'birthdate',
            # 'gender',

        ]
        
        exclude = ['password1','password2','username',]

        labels = {
                  }

        widgets = {
        }


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            
            'tournament',
            'day_time',
            'division',
            'level',
            'payment',
            'payment_cost',
            'payment_comment',
            'partner','conflicts','parent','parent_relation','email_parent','phone_parent',
            
            
        ]
        
        labels = {
            'tournament':'Select event*',
            'day_time':'Select day time*',
            'division':'Select division*',
            'level':'Select level*',
            'payment_comment':'Payment comment',
            'payment_cost':'Select entry fee*',
            'payment':'Select payment method*',
            'parent': 'Parent name',
            'parent_relation': 'Select parent relation',
            'email_parent': 'Email parent',
            'phone_parent': 'Phone parent',
                  
                  }

        widgets = {

        }
