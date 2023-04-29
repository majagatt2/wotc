from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from apps.tournament.views import TournamentPublicView,TournamentPrivView, TournamentDetail,RegistrationPublicCreate, RegistrationPrivCreate, ListRegistrationEventViewPublic
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', TournamentPublicView.as_view(), name='tournament_public'),
    path('members', login_required(TournamentPrivView.as_view()), name='tournament_members'),
    path('tournament_detail/<parameter>', TournamentDetail.as_view(),
         name='tournament_detail'),
    
    path('registration_public/<pk>', RegistrationPublicCreate.as_view(), name='registration_public'),
    path('registration_members/<pk>', login_required(RegistrationPrivCreate.as_view()),
         name='registration_members'),
    
    path('list_registered_event/<parameter>', ListRegistrationEventViewPublic.as_view(),
         name='list_registered_event'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
