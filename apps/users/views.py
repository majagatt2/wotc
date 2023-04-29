from django.shortcuts import render, redirect

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from apps.users.models import Person, FamilyMemberRelationship
from apps.member.models import Member, About
from apps.users.forms import RegisterForm, RegisterMemberFamilyForm, RelationshipForm, RelationshipMultiForm, UpdatePersonForm 
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
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
    form_class = UpdatePersonForm
    template_name = "users/edit_person.html"
    success_url = reverse_lazy('my_profile')
    success_message = "The data was updated successfully. Thank You!"
    
    def form_valid(self, form, **kwargs):
        form.instance.password = self.request.user.password
        form.save()
        return super().form_valid(form)

    
    
    
    
    

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
    
    def get_context_data(self, **kwargs):
        context = super(FamilyMemberDelete, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', None)
        context['person'] = Person.objects.filter(id=pk)
        return context
    


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
        context['family_user'] = FamilyMemberRelationship.objects.filter(
            person=self.request.user).order_by('id')
        context['persons'] = Person.objects.filter(id=self.request.user.id)
        context['status'] = Member.objects.filter(person=self.request.user).order_by('id')
      
        members_family = []
        family = FamilyMemberRelationship.objects.filter(
            person=self.request.user)
        for f in family:
            members_family.append(f.relation)
            
        members = Member.objects.all().order_by('id')
        members_list = []
        member_person_list = []
       
        for f in members_family:
            member_for_clean = []
            for member in members:
                if f == member.person:
                    if len(member_for_clean) == 0:
                       
                        member_for_clean.append(member)
                    
                    elif len(member_for_clean) > 0:
                        for m in member_for_clean:
                            if m.person == member.person:
                                if member.id > m.id:
                                    member_for_clean.remove(m)
                                    member_for_clean.append(member)
                            else:
                                member_for_clean.append(member)
            if len(member_for_clean) > 0:
                for m in member_for_clean:
                    members_list.append(m)
                    member_person_list.append(m.person)
                    
                    member_for_clean = []
                
        context['family_groups'] = FamilyMemberRelationship.objects.filter(relation=self.request.user)
        context['all_members'] = Member.objects.all().order_by('id')
        context['members_list'] = members_list
        context['member_person'] = member_person_list
        context['members_family'] = members_family
        return context
    
    


