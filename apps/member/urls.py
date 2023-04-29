from django.conf import settings
from apps.member.views import MemberRegister,  email_alert_member
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('active_member/<pk>', login_required(MemberRegister.as_view()), name='active_member'),
    path('email_alert_member/', email_alert_member, name='email_alert_member'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
