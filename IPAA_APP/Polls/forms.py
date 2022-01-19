from dataclasses import field
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import NON_FIELD_ERRORS
from django import forms

from Polls.models import Usuario
#from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = "__all__"
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
