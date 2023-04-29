from django import forms
from django.forms.fields import DateField
from apps.tournament.models import Payment
from apps.member.models import Member, CostsMembers, TypeMember
from django.core.mail import send_mail




class MemberForm(forms.ModelForm):
    
    # type_member = forms.ModelChoiceField(queryset=TypeMember.objects.all())
    payment_cost = forms.ModelChoiceField(
        label='Select payment cost', queryset=CostsMembers.objects.all())
    
    payment_method = forms.ModelChoiceField(label='Select payment method',queryset=Payment.objects.all())
    # amount = forms.ModelChoiceField(queryset=CostsMembers.objects.all())
    # date_activate = DateField(label='Date start your Membership',
    #                       widget=forms.widgets.DateInput(attrs={'type': 'date', }))

    class Meta:
        model = Member
        fields = [
           
            'person',
            'date_period',
            'type_member',
            'payment_cost',
            'amount',
            'payment_method',
            'payment_comment',

        ]

        labels = {
            'person': 'You are about to activate:',
            'date_period': 'Current Period ',
            'type_member':'Select member type',
            #'payment_cost': 'Select member cost',
            'amount': 'Please, select amount to paid',
            #'payment_method':'Payment method',
            'payment_comment': 'Payment comment',
                  }

        widgets = {
            # 'date_period':  forms.Select(attrs={'class': 'form-control'}),

        }
