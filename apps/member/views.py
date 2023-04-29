from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from apps.member.forms import MemberForm
from apps.member.models import Member, MemberPeriod, CostsMembers, TypeMember
from apps.users.models import Person
from apps.tournament.models import Payment
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.mail import send_mail, mail_admins, EmailMultiAlternatives, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.


def error_404_view(request, exception):
    return render(request, 'base/pages-error-404.html')

def email_alert_member(request):
     send_mail('New Member',
               'a new member requires validation',
               ['marianogattesco@gmail.com',],
               fail_silently=False)
     return render(request,'general/email/email_admin_member_alert.html')



class MemberRegister(SuccessMessageMixin,CreateView):
    model = Member
    template_name = "member/form_register_member.html"
    form_class = MemberForm
    success_url = reverse_lazy("my_profile")
    success_message = "Thank You!"
    
    
    def get_context_data(self, **kwargs):
        context = super(MemberRegister,
                        self).get_context_data(**kwargs)
        filtro = self.kwargs.get('pk', None)
        context['member_family'] = Person.objects.filter(id=filtro)
        context['period'] = MemberPeriod.objects.filter(id=True)
        context['types'] = TypeMember.objects.all()
        context['payment_costs'] = CostsMembers.objects.all()
        context['payment_method'] = Payment.objects.all()
        return context
    
    def form_valid(self, form, **kwargs):
       
        
       
        form.save()
           
        
        # template = render_to_string(
        #     'email/email_admin_member_alert.html', {'member': person})
        # subject = f"NEW MEMBER {person}"
        # from_email = settings.EMAIL_HOST_USER
        # to_email = settings.EMAIL_HOST_USER
        # msg = EmailMessage(subject, template, from_email, [to_email])
        # msg.content_subtype = "html"
        # msg.fail_silently = False
        # msg.send()
        
        
        # template2 = render_to_string(
        #     'email/email__member_thanks.html', {'member': person})
        # subject2 = f"WELCOME {person}"
        # to_email2 = person.email
        # msg2 = EmailMessage(subject2, template2, from_email, [to_email2])
        # msg2.content_subtype = "html"
        # msg2.fail_silently = False
        # msg2.send()
        
        return super().form_valid(form)
    
   
        
        
        

    # send_mail(
    #     'New Member',
    #     'A new member needs to be validated.',
    #     settings.EMAIL_HOST_USER,
    #     [settings.EMAIL_HOST_USER],
    #     fail_silently=False,
    # )

    
 
    
    # subject = "NEW MEMBER"
    # from_email = settings.EMAIL_HOST_USER
    # to_email = settings.EMAIL_HOST_USER
    # html_content = f"<p>Please go to Admin and <stong>validate to {member.first_name} </strong></p>"
    # msg = EmailMessage(subject, html_content, from_email, [to_email])
    # msg.content_subtype = "html"  # Main content is now text/html
    # msg.send()


