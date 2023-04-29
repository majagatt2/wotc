from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from apps.users.views import UserCreate, UserUpdate, FamilyMemberUpdate,FamilyMemberDelete,MyProfile, UserCreateGroups
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetCompleteView, PasswordResetDoneView, PasswordResetConfirmView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
   
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(template_name='http://wotennisclub.weebly.com/'), name='logout'),
    
    path('password_reset/', PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html'), name='password_reset'),

    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    
    
    
    # path('login', login2, name='login'),
    path('register', UserCreate.as_view(), name='register'),
    path('register_group', login_required(UserCreateGroups.as_view()), name='register_group'),
    # path('register_relationship', login_required(
    #     CreateRelationShips.as_view()), name='register_relationship'),
    path('my_profile', login_required(MyProfile.as_view()), name='my_profile'),
    path(r'edit_person/<pk>', login_required(UserUpdate.as_view()), name='edit_person'),
    path(r'edit_family_member/<pk>', login_required(FamilyMemberUpdate.as_view()), name='edit_family_member'),
    path('delete_family_member/<pk>',
         login_required(FamilyMemberDelete.as_view()), name='delete_family_member'),
    
    
    
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
