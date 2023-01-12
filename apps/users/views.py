from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from apps.users.models import Person, FamilyMemberRelationship
from apps.member.models import Member, About
from apps.users.forms import RegisterForm, RegisterMemberFamilyForm, RelationshipForm, RelationshipMultiForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
#from bootstrap_modal_forms.generic import BSModalCreateView

from django.urls import reverse_lazy
# Create your views here.


def error_404_view(request, exception):
    return render(request, 'base/pages-error-404.html')



# def login2(request):
#     return render(request,'users/registration/login.html')


class UserCreate(SuccessMessageMixin, CreateView):
    model = Person
    template_name = "users/form_register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    success_message = "Thank You! Please, now you need to log in to your account for complete your membership"
    
    def get_context_data(self, **kwargs):
        context = super(UserCreate,
                        self).get_context_data(**kwargs)
        context['about'] = About.objects.all()
        return context
    
    
    
    
    

class UserUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Person
    form_class = RegisterForm
    template_name = "users/edit_person.html"
    success_url = reverse_lazy('login')
    success_message = "The data was updated successfully. Please login again. Thank You!"
    

class FamilyMemberUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Person
    form_class = RegisterMemberFamilyForm
    template_name = "users/edit_family_member.html"
    success_url = reverse_lazy('my_profile')
    success_message = "The data was updated successfully!"

    # def get_form_kwargs(self):
    #     kwargs = super(FamilyMemberUpdate, self).get_form_kwargs()
    #     kwargs.update(instance={
    #         'member': self.object,
    #         'relation': self.family_members.relation_type,
    #     })
    #     return kwargs
    
    
class FamilyMemberDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Person
    success_url = reverse_lazy('my_profile')
    template_name = "users/delete_family_member.html"
    success_message = "This has been successfully removed!"
    


#adress', 'city', 'state', 'zip','email',
class UserCreateGroups(CreateView):
    model = Person
    template_name = "users/form_family_register.html"
    form_class = RelationshipForm
    second_form = RegisterMemberFamilyForm
    success_url = reverse_lazy("my_profile")
    
    def get_context_data(self, **kwargs):
        context = super(UserCreateGroups, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form(request.POST)
        if form.is_valid() and form2.is_valid():
            nueva = form.save(commit=False)
            nueva.person = self.request.user
            nueva.relation = form2.save(commit=False)
            nueva.relation.zip = self.request.user.zip
            nueva.relation.adress = self.request.user.adress
            nueva.relation.city = self.request.user.city
            nueva.relation.state = self.request.user.state
            nueva.relation.password = self.request.user.password
            nueva.relation.save()
            nueva.save()
        return redirect(self.get_success_url())

    
class MyProfile(ListView):
    model = Person
    template_name = 'users/my_profile.html'
    
    
    def get_context_data(self, **kwargs):
        context = super(MyProfile,
                        self).get_context_data(**kwargs)
        context['family_user'] = FamilyMemberRelationship.objects.filter(person=self.request.user)
        context['member'] = Person.objects.filter(id=self.request.user.id)
        context['status'] = Member.objects.filter(person=self.request.user)
      
        family_group = {}
        members_family = []
        family = FamilyMemberRelationship.objects.filter(
            person=self.request.user)
        for f in family:
            members_family.append(f.relation)
            
       
        
        members_list = []
        for member in Member.objects.all():
            if member.get_status:
                members_list.append(member.person.id)
                
        context['family_groups'] = FamilyMemberRelationship.objects.filter(relation=self.request.user)
        context['all_members'] = Member.objects.all()
        context['members_list'] = members_list
        return context
    