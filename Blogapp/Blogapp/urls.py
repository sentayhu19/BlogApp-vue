from django.contrib import admin
from django.urls import path,include, re_path

#handling django-registration user reistration form for custom model
from django_registration.backends.one_step.views import RegistrationView
from users.forms import UserForm
from main.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    #provides auth urls(login and logout) via the browserble api
    path('auth/', include('rest_framework.urls')),
    path('api/', include('users.urls')),
    #articles
    path('api/', include('articles.urls')),
  
    ############ django-registration  ##########
    path('accounts/register/',
        RegistrationView.as_view(
            form_class=UserForm,
            success_url = "/",
        ),
        name='django_registration_register',
    ),
    path('accounts/', include('django.contrib.auth.urls')),

    ############django-rest-auth##########
    #django-rest-auth urls (login/out/password reset/confirm etc..)
    path('rest-auth/', include('rest_auth.urls')), 
     
    #django-rest-auth.registration urls (provides url for reg,email ver, etc)
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    
    #redirect every request to index.html
   re_path(r'^.*$', Index.as_view(), name = "index"),#catch all urls
]