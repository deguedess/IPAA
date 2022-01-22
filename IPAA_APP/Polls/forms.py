import datetime

from dataclasses import field
from django.core.exceptions import NON_FIELD_ERRORS
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from Polls.models import Usuario
#from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        widgets = {
            'idade': forms.NumberInput(attrs={
                'autofocus': True
            })
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['perfil'].required = False
