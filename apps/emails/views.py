from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, UpdateView, View, DeleteView, CreateView
from apps.emails.models import Newsletter
from apps.emails.forms import NewsletterCreationForm
from apps.users.models import Person
from apps.member.models import Member
from apps.tournament.models import Tournament, Registration
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.contrib.messages.views import SuccessMessageMixin
from django.template.loader import render_to_string

from django.urls import reverse_lazy


# Create your views here.

def error_404_view(request, exception):
    return render(request, 'base/pages-error-404.html')


class DashboardHomeView(TemplateView):
    template_name = "emails/desk_emails.html"


# class NewsletterCreateView(View):
    
    
#     def get(self, request, *args, **kwargs):
#         form = NewsletterCreationForm()
        
#         email_people_all = []
#         for p in Person.objects.all():
#             email_people_all.append(p.email)
#         email_members = []
#         for m in Member.objects.filter(is_member=True):
#             if m.get_status == True:
#                 email_members.append(m.person.email)
#         # options = {'all_people':email_people_all,'members':email_members}
#         options = ['marianogattesco@gmail.com']
        
        
#         context = {
#             'form': form,
#             'options': options
#         }
#         return render(request, 'emails/form_email.html', context)

#     def post(self, request, *args, **kwargs):
#         if request.method == "POST":
#             form = NewsletterCreationForm(request.POST or None)

#             if form.is_valid():
#                 instance = form.save()
#                 newsletter = Newsletter.objects.get(id=instance.id)

#                 if newsletter.status == "Published":
#                     subject = newsletter.subject
#                     body = newsletter.body
#                     from_email = settings.EMAIL_HOST_USER
#                     to = newsletter.email
#                     send_mail(subject=subject, 
#                               from_email=from_email, 
#                               recipient_list=[to], 
#                               message=body,
#                               fail_silently=True)
#                 return redirect('emails:desk_email')
#             else:
#                 print("no anda")

#         context = {
#             'form': form
#         }
#         return render(request, 'emails/form_email.html', context)

class NewsletterCreateView(SuccessMessageMixin,CreateView):
    model = Newsletter
    tournaments = []
    email_members = []
    template_name = "emails/form_email.html"
    form_class = NewsletterCreationForm
    success_url = reverse_lazy("create_email")
    success_message = "The email was sent successfully !"
    
    for m in Member.objects.filter(is_member=True):
        if m.get_status == True:
            if m.person.email in email_members:
                pass
            else:
                email_members.append(m.person.email)
            
    for t in Tournament.objects.filter(condition=True):
        tournaments.append(t.id)

    def get_context_data(self, **kwargs):
        context = super(NewsletterCreateView,
                        self).get_context_data(**kwargs)
        
        email_people_all = []
        groups = []
        
        for p in Person.objects.all():
            if p.email in email_people_all:
                pass
            else:
                email_people_all.append(p.email)
        for n in range(1):
            email_people_all.insert(0,'wheelingoglebaytennisclub@gmail.com')
            
        # for t in Tournament.objects.filter(condition=True):
        #     email_people_all.insert(0,t.id)
            
        for n in range(1):
            groups.insert(0,'Members')
        for n in range(1):
            groups.insert(0, 'Nobody')
            
        
        all = email_people_all
        context['all'] = all
        context['groups'] = groups
        context['tournament'] = Tournament.objects.filter(condition=True)
        return context
    
    def form_valid(self, form, **kwargs):
        instance = form.save()
       
        if instance.status == "Published":
            template = render_to_string(
                'emails/email.html', {'body': instance.body})
            try:
                instance_bcc = int(instance.bcc)
            except ValueError:
                instance_bcc = instance.bcc
                
            subject = instance.subject
            body = instance.body
            from_email = settings.EMAIL_HOST_USER
                        
            if instance_bcc == "Members":
                to = [instance.email]
                bcc = self.email_members
                print("emails members")
            
            elif type(instance_bcc) == int:
                emails_tournament = []
                for t in self.tournaments:
                   
                    if t == instance_bcc:
                        for r in Registration.objects.filter(tournament=t):
                            print(r.person.email)
                            emails_tournament.append(r.person.email)
                to = [instance.email]
                bcc = emails_tournament
            elif instance_bcc == "Nobody":
                to = [instance.email]
                bcc = []
                
            print(f'tipo instancia {type(instance.email)}')
            print(f'instancia {instance.email}')
            print(f'enviado a {to}')
            print(f'enviado BCC a {bcc}')
            msg= EmailMessage(subject,template,from_email,to, bcc=bcc)
            msg.content_subtype = "html"
            msg.fail_silently = False
            msg.send()
            # send_mail(subject, body, from_email, 
            #                         to,  fail_silently=True)
        else:
            print("no published")
        
        return super().form_valid(form)

        


# class NewslettersDashboardHomeView(View):
#     def get(self, request, *args, **kwargs):
#         newsletters = Newsletter.objects.all()

#         context = {
#             'newsletters': newsletters
#         }
#         return render(request, 'dashboard/list.html', context)


class NewsletterDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        newsletter = get_object_or_404(Newsletter, pk=pk)
        context = {
            'newsletter': newsletter
        }
        return render(request, 'emails/desk_emails.html', context)




# class NewsletterUpdateView(UpdateView):
#     model=Newsletter
#     form_class=NewsletterCreationForm
#     template_name='dashboard/update.html'
#     success_url='/dashboard/detail/2/'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update({
#             'view_type':'update'
#         })
#         return context



# class NewsletterDetailView(View):
#     def get(self, request, pk, *args, **kwargs):
#         newsletter = get_object_or_404(Newsletter, pk=pk)
#         context = {
#             'newsletter': newsletter
#         }
#         return render(request, 'dashboard/detail.html', context)


#     def post(self, request, pk, *args, **kwargs):
#         newsletter=get_object_or_404(Newsletter, pk=pk)

#         if request.method=="POST":
#             form=NewsletterCreationForm(request.POST or None)

#             if form.is_valid():
#                 instance=form.save()
#                 newsletter=Newsletter.objects.get(id=instance.id)

#                 if newsletter.status=="Published":
#                     subject = newsletter.subject
#                     body = newsletter.body
#                     from_email = settings.EMAIL_HOST_USER
#                     for email in newsletter.email.all():
#                         send_mail(subject=subject, from_email=from_email, recipient_list=[email], message=body, fail_silently=True)
#                 return redirect('dashboard:detail', pk=newsletter.id)
#             return redirect('dashboard:detail', pk=newsletter.id)
#         else:
#             form=NewsletterCreationForm(instance=newsletter)

#         context={
#             'form':form        
#         }
#         return render(request, 'dashboard/update.html', context)


# class NewsletterDeleteView(DeleteView):
#     model=Newsletter
#     template_name='dashboard/delete.html'
#     success_url='/dashboard/list/'