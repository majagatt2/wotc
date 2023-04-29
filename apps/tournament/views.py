from django.shortcuts import render,redirect
from apps.users.models import Person
from apps.tournament.models import Tournament
from apps.tournament.forms import *
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
import uuid
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage

# Create your views here.


def error_404_view(request, exception):
    return render(request, 'base/pages-error-404.html')


class TournamentPublicView(ListView):
    model = Tournament
    queryset = Tournament.objects.filter(public=True).order_by("date")
    template_name = 'tournament/tournaments_public.html'
    

class TournamentPrivView(ListView):
    model = Tournament
    queryset = Tournament.objects.filter(members=True).order_by("date")
    template_name = 'tournament/tournaments_members.html'
    
class TournamentDetail(ListView):
    model = Tournament
    template_name = 'tournament/tournaments_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TournamentDetail, self).get_context_data(**kwargs)
        parameter = self.kwargs.get('parameter', None)
        context['tournament'] = Tournament.objects.filter(id=parameter)
        return context

    # def form_valid(self, form):
    #     if self.request.user:
    #         form.instance.persona = self.request.user
    #     return super().form_valid(form)


class RegistrationPublicCreate(SuccessMessageMixin, CreateView):
    model = Person
    template_name = "tournament/form_publ_registration.html"
    form_class = PersonForm
    second_form = RegistrationForm
    success_url = reverse_lazy("tournament_public")
    success_message = "Thank You for registering!"
    

    def get_context_data(self, **kwargs):
        context = super(RegistrationPublicCreate, self).get_context_data(**kwargs)
        filtro = self.kwargs.get('pk', None)
        context['tournament'] = Tournament.objects.filter(id=filtro)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form(self.request.GET)
        return context

    def post(self, request, *args, **kwargs ):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form(request.POST)
        if form.is_valid() and form2.is_valid():
            nueva = form.save(commit=False)
            nueva.password = make_password('sin password')
            nueva.username = uuid.uuid4().hex[:9]
            nueva.save()
            nuevo = form2.save(commit=False)
            nuevo.person = nueva
            nuevo.save()
            
            template = render_to_string(
                'email/email_admin_registered_alert.html', {'person': nueva, 'event':nuevo.tournament})
            subject = f"NEW EVENT REGISTRATION {nueva}"
            from_email = settings.EMAIL_HOST_USER
            to_email = settings.EMAIL_HOST_USER
            msg = EmailMessage(subject, template, from_email, [to_email])
            msg.content_subtype = "html"
            msg.fail_silently = False
            msg.send()

            template2 = render_to_string(
                'email/email__registration_thanks.html', {'person': nueva, 'event': nuevo.tournament})
            subject2 = f"THANKS {nueva}"
            to_email2 = nueva.email
            msg2 = EmailMessage(subject2, template2, from_email, [to_email2])
            msg2.content_subtype = "html"
            msg2.fail_silently = False
            msg2.send()
            self.success_message = "Thank You for registering!"
                
        return redirect(self.get_success_url())
    


class RegistrationPrivCreate(SuccessMessageMixin, CreateView):
    model = Registration
    template_name = "tournament/form_priv_registration.html"
    form_class = RegistrationForm
    
    success_url = reverse_lazy("tournament_members")
    success_message = "Thank You for registering!"
    
    def form_valid(self, form, **kwargs):
        form.instance.person = self.request.user
        person = form.instance.person
        tournament = form.instance.tournament
        form.save()
        
        # template = render_to_string(
        #     'email/email_admin_registered_alert.html', {'person': person, 'event': tournament})
        # subject = f"NEW EVENT REGISTRATION {person}"
        # from_email = settings.EMAIL_HOST_USER
        # to_email = settings.EMAIL_HOST_USER
        # msg = EmailMessage(subject, template, from_email, [to_email])
        # msg.content_subtype = "html"
        # msg.fail_silently = False
        # msg.send()
        
        # template2 = render_to_string(
        #     'email/email__registration_thanks.html', {'person': person, 'event': tournament})
        # subject2 = f"THANKS {person}"
        # to_email2 = person.email
        # msg2 = EmailMessage(subject2, template2, from_email, [to_email2])
        # msg2.content_subtype = "html"
        # msg2.fail_silently = False
        # msg2.send()

        
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(RegistrationPrivCreate,
                        self).get_context_data(**kwargs)
        filtro = self.kwargs.get('pk', None)
        tournament = Tournament.objects.filter(id=filtro)
        
        name = ''
        for n in tournament:
            name = n.name 
        
        context['tournament'] = tournament
        context['tournament_name'] = name
        context['person'] = Person.objects.filter(id=self.request.user.id)
        return context


class ListRegistrationEventViewPublic(ListView):
    model = Registration
    template_name = 'Public_/list_registered_events.html'
    ordering = []

    def get_context_data(self, **kwargs):
        context = super(ListRegistrationEventViewPublic,
                        self).get_context_data(**kwargs)
        parameter = self.kwargs.get('parameter', None)
        context['tournament'] = Tournament.objects.filter(id=parameter)
        context['registers'] = Registration.objects.filter(tournament=parameter)
        return context



