
from django.contrib import admin
from django.urls import path,include
from users.forms import UserForm
from django_registration.backends.one_step.views import RegistrationView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/',RegistrationView.as_view(
    form_class = UserForm,
    success_url ="/"  ,
    ), name="register"
    ),
    path('accounts/',include('django.contrib.auth.urls')),

    path('auth/',include('rest_framework.urls')),
    path('rest-auth/',include('rest_auth.urls')),
    path('rest-auth/registration',include('rest_auth.registration.urls')),
]
 
