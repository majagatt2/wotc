from django import forms
from django.forms.fields import DateField
from apps.member.models import Member

class MemberForm(forms.ModelForm):
    
    # date_activate = DateField(label='Date start your Membership',
    #                       widget=forms.widgets.DateInput(attrs={'type': 'date', }))

    class Meta:
        model = Member
        fields = [
           
            'person',
            'date_period',
            

        ]

        labels = {
            'person':'You are about to activate:',
            'date_period':'Current Period ',
                  }

        widgets = {
            # 'date_period':  forms.Select(attrs={'class': 'form-control'}),

        }
