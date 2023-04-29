from django import forms
from .models import Newsletter 
from apps.tournament.models import Tournament, Registration
from apps.users.models import Person
from apps.member.models import Member



class NewsletterCreationForm(forms.ModelForm):
    
    class Meta:
        model = Newsletter
        fields = [ 'subject', 'body', 'email', 'bcc' ,'status']

        labels = {

            #'name': 'Name',
            'subject': 'Subject',
            'body': 'Body',
            'email': 'To:',
            'bcc':"BCC",
            'status': 'Status',

        }

        widgets = {

            #'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            #'email': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            
            
            


        }
