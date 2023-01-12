from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from apps.member.forms import MemberForm
from apps.member.models import Member, MemberPeriod
from apps.users.models import Person
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
# Create your views here.


def error_404_view(request, exception):
    return render(request, 'base/pages-error-404.html')



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
        return context

    # def form_valid(self, form, **kwargs):
    #     period = 
    #     form.instance. = 
    #     form.save()
    #     return super().form_valid(form)
    
    
class MemberRegisterModal(CreateView):
    model = Member
    template_name = "users/my_profile.html"
    form_class = MemberForm
    success_url = reverse_lazy("my_profile")
    success_message = "Thank You!"

    def form_valid(self, form, **kwargs):
        form.instance.person = self.request.user
        form.save()
        return super().form_valid(form)
   
    
    