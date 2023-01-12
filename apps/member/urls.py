from django.conf import settings
from apps.member.views import MemberRegister, MemberRegisterModal
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('active_member/<pk>', login_required(MemberRegister.as_view()), name='active_member'),
    path('active_modal/<pk>', login_required(MemberRegisterModal.as_view()),
         name='active_modal'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
