from django.contrib.auth.models import User
from django.forms.fields import DateField
#from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms
from betterforms.multiform import MultiModelForm
from django.contrib.auth.forms import UserCreationForm
from apps.users.models import Person, FamilyMemberRelationship


class RegisterForm(UserCreationForm):
    birthdate = DateField(label='Date of Birth',
        widget=forms.widgets.DateInput(attrs={'type': 'date', }))
    ntrp_rating = forms.CharField(
        label='NTRP_rating',required=False, widget=forms.TextInput(attrs={'placeholder':'Optional, if you have one'}))
    email = forms.EmailField(label='Email adress', required=True)
    phone = forms.CharField(max_length=11, required=False)

    class Meta:
        model = Person
        fields = [
            
            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'adress', 'city', 'state','zip', 'birthdate','ntrp_rating', 'gender',  'profilePicture',

        ]

        labels = {
           
                  }

        widgets = {
            
            
            
        }
        
        #'adress', 'city', 'state', 'zip','email',


class RegisterMemberFamilyForm(forms.ModelForm):
    birthdate = DateField(label='Date of Birth',
                          widget=forms.widgets.DateInput(attrs={'type': 'date', }))
    
    ntrp_rating = forms.CharField(
        label='NTRP_rating', required=False, widget=forms.TextInput(attrs={'placeholder': 'Optional, if you have one'}))
    
    email = forms.EmailField(label='Email adress', required=False)
    
   
    class Meta:
        model = Person
        fields = [

            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'birthdate', 'ntrp_rating', 'gender',
            'profilePicture',
            
        ]

        labels = {'profilePicture': 'Profile Picture',
                  }

        widgets = {
            

        }


class RelationshipForm(forms.ModelForm):
    
    class Meta:
        model = FamilyMemberRelationship
        fields = [

            
            'relation_type',

        ]


class RelationshipMultiForm(MultiModelForm):
    form_classes = {
        'member': RegisterMemberFamilyForm,
        'relation': RelationshipForm,
    }
    
    
class UpdatePersonForm(forms.ModelForm):
    
    birthdate = DateField(label='Date of Birth',
                          widget=forms.widgets.DateInput(attrs={'type': 'date', }))
    ntrp_rating = forms.CharField(
        label='NTRP_rating', required=False, widget=forms.TextInput(attrs={'placeholder': 'Optional, if you have one'}))
    email = forms.EmailField(label='Email adress', required=True)

    class Meta:
        model = Person
        exclude = ['password1', 'password2', ]
        
        fields = [

            'first_name',
            'last_name',
            'username',
            'email',
            'phone',
            'adress', 'city', 'state', 'zip', 'birthdate', 'ntrp_rating', 'gender',  'profilePicture',

        ]

        labels = {

        }

        widgets = {



        }



