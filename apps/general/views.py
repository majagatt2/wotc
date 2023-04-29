from django.shortcuts import render
# from apps.general.models import About
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from apps.general.models import Volunteer, Activities, OtherEvent
from apps.users.models import Person
from apps.tournament.models import Registration, Tournament
from apps.member.models import Member, TypeMember
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.general.forms import VolunteerForm

# Create your views here.


def error_404_view(request, exception):
    return render(request, 'base/pages-error-404.html')


def principal(request):
    return render(request, 'base/start.html')


def principal_member(request):
    return render(request, 'base/start.html')


def index_forms(request):
    return render(request, 'base/index_forms.html')


def payments(request):
    return render(request, 'base/payments.html')


def desk_email(request):
    return render(request, 'email/desk_emails.html')




# class AboutView(ListView):
#     model = About
#     template_name = 'base/about.html'
    
class ListPersonView(ListView):
    model = Person
    template_name = 'admin/list_persons.html'
    ordering = ['last_name']
    

class ListMemberView(ListView):
    model = Member
    template_name = 'admin/list_members.html'
    ordering = ['person']
    
    def get_context_data(self, **kwargs):
        context = super(ListMemberView, self).get_context_data(**kwargs)
        
        members=[]
        for m in Member.objects.all():
            if m.is_member and m.get_status:
                members.append(m)
        
        context['members'] = members
        return context
    
class ListMemberViewPark(ListView):
    model = Member
    template_name = 'public_/wheeling_park.html'
    ordering = ['person']

    def get_context_data(self, **kwargs):
        context = super(ListMemberViewPark, self).get_context_data(**kwargs)

        members = []
        for m in Member.objects.all():
            if m.is_member and m.get_status:
                members.append(m)
                

        context['members'] = members
        return context


    
    
        

class ListActivitiesView(ListView):
    model = Activities
    queryset = Activities.objects.filter(status=True)
    template_name = 'volunteer/available_activities.html'
    ordering = ['day',]

    def get_context_data(self, **kwargs):
        context = super(ListActivitiesView, self).get_context_data(**kwargs)
        context['other_event'] = OtherEvent.objects.all()
        return context





class VolunteerCreate(SuccessMessageMixin,CreateView):
    model = Volunteer
    template_name = "volunteer/form_register_volunteer.html"
    form_class = VolunteerForm
    success_url = reverse_lazy("activities")
    success_message = "Thank You!"
    
    def get_context_data(self, **kwargs):
        context = super(VolunteerCreate, self).get_context_data(**kwargs)
        parameter = self.kwargs.get('pk', None)
        context['activities'] = Activities.objects.filter(id=parameter)
        return context
    

class ListVolunteerView(ListView):
    model = Volunteer
    template_name = 'admin/list_volunteers.html'
    ordering = []

    def get_context_data(self, **kwargs):
        context = super(ListVolunteerView, self).get_context_data(**kwargs)
        
        context['other_event'] = OtherEvent.objects.all()
        context['activities'] = Activities.objects.filter(status=True)
        return context



class ListRegistrationEventView(ListView):
    model = Registration
    template_name = 'admin/list_register_events.html'
    ordering = []

    def get_context_data(self, **kwargs):
        context = super(ListRegistrationEventView, self).get_context_data(**kwargs)
        parameter = self.kwargs.get('parameter', None)
        context['tournaments'] = Tournament.objects.filter(id=parameter)
        return context



class ListStadistics(ListView):
    model = Member
    template_name = 'admin/stadistics.html'
    
    def get_context_data(self, **kwargs):
        context = super(ListStadistics,
                        self).get_context_data(**kwargs)
        
        
        members_by_type = {}
        count=0
        for t in TypeMember.objects.all():
            for m in Member.objects.filter(type_member=t, is_member=True):
                if m.get_status:
                    count += 1
                    
            members_by_type.update({t: count})
            count = 0
                   
        
        members = 0
        for m in Member.objects.filter(is_member=True):
            if m.get_status:
                members += 1
        
        event = {}
        for t in Tournament.objects.filter(condition=True):
            registered = 0
            registered_true = 0
            registered_false = 0
            if Registration.objects.filter(tournament=t):
                for r in Registration.objects.filter(tournament=t):
              
                    registered += Registration.objects.filter(tournament=t).count()
                    registered_true += Registration.objects.filter(tournament=t,condition=True).count()
                    registered_false += Registration.objects.filter(
                        tournament=t, condition=False).count()
                    event.update({t:[registered,registered_true,registered_false]})
                    registered = 0
                    registered_true = 0
                    registered_false = 0
            else:
                event.update({t: [registered, registered_true, registered_false]})
                    
        event_payments = {}
        for t in Tournament.objects.all():
            registered = 0
            payments = 0
            registry = Registration.objects.filter(tournament=t)
            if  registry:
                for r in registry:
                    registered += Registration.objects.filter(tournament=t, condition=True).count()
                    if Registration.objects.filter(tournament=t, condition=True):
                        payments += r.payment_cost.price
                    event_payments.update({t: [registered,payments]})
                    registered = 0
                payments = 0
            else:
                event_payments.update({t: [registered, payments]})
                    
           
                   
                
        
        context['people'] = Person.objects.all()
        context['members'] = members
        context['members_by_type'] = members_by_type
        
        context['tournaments'] = Tournament.objects.filter(condition=True)
        context['tournaments_all'] = Tournament.objects.all()
        context['payments'] = event_payments
        context['registered'] = event
        
        return context
    
class TournamentsAdmin(ListView):
    model = Tournament
    #queryset = Tournament.objects.all().order_by('-date')
    template_name = 'admin/list_by_events.html'

    def get_context_data(self, **kwargs):
        context = super(TournamentsAdmin, self).get_context_data(**kwargs)
        # parameter = self.kwargs.get('parameter', None)
        context['tournaments'] = Tournament.objects.all()
        
        event = {}
        for t in Tournament.objects.all():
            registered = 0
            registered_true = 0
            registered_false = 0
            if Registration.objects.filter(tournament=t):
                for r in Registration.objects.filter(tournament=t):

                    registered += Registration.objects.filter(
                        tournament=t).count()
                    registered_true += Registration.objects.filter(
                        tournament=t, condition=True).count()
                    registered_false += Registration.objects.filter(
                        tournament=t, condition=False).count()
                    event.update(
                        {t: [registered, registered_true, registered_false]})
                    registered = 0
                    registered_true = 0
                    registered_false = 0
            else:
                event.update(
                    {t: [registered, registered_true, registered_false]})
                
            context['registered'] = event
        
        return context

    
