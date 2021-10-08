from django_registration.forms import RegistrationForm

from .models import UserModel


class UserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = UserModel 