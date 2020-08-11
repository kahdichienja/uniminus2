from django.urls import path, include
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static

appname = 'accounts'

urlpatterns = [
    path('', user_account_profile, name = 'profile'),
    path('dashboard/', user_dashboard, name = 'dashboard'),
    path('create/', user_create_profile, name = 'profile_create'),
    path('login/', user_login, name = 'user_login'),
    path('register/', user_register, name = 'user_register'),

    # new urls
    path('userRUCF1/', userRUCF1Formview, name='userRUCF1Formview'),
    path('userRUM/', userRUMFormview, name='userRUMFormview'),
    path('userRUCF2/', userRUCF2Formview, name='userRUCF2Formview'),
    path('userRUCA1/', userRUCA1Formview, name='userRUCA1Formview'),
    # end new urls


    path('student/', create_and_auth_then_redirect, name = 'create_and_auth_then_redirect'),
    path('student/profile/', create_prof_then_redirect_to_another_then_log_out, name='create_prof_then_redirect_to_another_then_log_out'),
    path('logout/', user_logout, name = 'user_logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)