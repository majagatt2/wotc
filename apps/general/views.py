from django.shortcuts import render
# from apps.general.models import About
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from apps.general.models import Volunteer, Activities, OtherEvent
from apps.users.models import Person
from apps.tournament.models import Registration, Tournament
from apps.member.models import Member
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
    
    
    
    
    
    

class ListActivitiesView(ListView):
    model = Activities
    queryset = Activities.objects.filter(status=True)
    template_name = 'volunteer/available_activities.html'
    ordering = []

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
        context['tournaments'] = Tournament.objects.filter(condition=True)
        return context
