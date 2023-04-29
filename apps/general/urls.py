from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from apps.general.views import  principal, principal_member,  index_forms, payments, ListPersonView, ListMemberView, VolunteerCreate, ListActivitiesView, ListVolunteerView, ListRegistrationEventView, ListMemberViewPark, ListStadistics,TournamentsAdmin
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
    path('wheeling_park_list', ListMemberViewPark.as_view(),
         name='wheeling_park_list'),
    path('list_volunteers/', login_required(ListVolunteerView.as_view()), name='list_volunteers'),
    
    path('list_register_event/<parameter>', login_required(ListRegistrationEventView.as_view()),
         name='list_register_event'),
    
    path('list_by_event/', login_required(TournamentsAdmin.as_view()),
         name='list_by_event'),

    
    path('stadistics/', login_required(ListStadistics.as_view()),
         name='stadistics'),
   
    

    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
