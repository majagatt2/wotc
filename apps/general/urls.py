from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from apps.general.views import  principal, principal_member,  index_forms, payments, ListPersonView, ListMemberView, VolunteerCreate, ListActivitiesView, ListVolunteerView, ListRegistrationEventView
from django.contrib.auth.decorators import login_required


urlpatterns = [

    
    path('', principal, name='main'),
    path('index_forms', index_forms, name='index_forms'),
    path('main_member', login_required(principal_member), name='main_member'),
    # path('about', AboutView.as_view(), name='about'),
    path('payments', payments, name='payments'),
    path('list_persons', login_required(ListPersonView.as_view()), name='list_persons'),
    path('list_members', login_required(
        ListMemberView.as_view()), name='list_members'),
    
    
    path('activities', ListActivitiesView.as_view(), name='activities'),
    path('volunteer/<pk>', VolunteerCreate.as_view(), name='volunteer'),
    path('list_volunteers/', login_required(ListVolunteerView.as_view()), name='list_volunteers'),
    path('list_register_event/', login_required(ListRegistrationEventView.as_view()),
         name='list_register_event'),

    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
