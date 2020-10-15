from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control',
                                                     'aria-describedby': 'inputGroup-sizing-default'})
        self.fields['email'].widget.attrs.update({'class': 'form-control',
                                                     'aria-describedby': 'inputGroup-sizing-default'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control',
                                                  'aria-describedby': 'inputGroup-sizing-default'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control',
                                                  'aria-describedby': 'inputGroup-sizing-default'})


class TaskAdd(forms.Form):
    text = forms.CharField(max_length=75,
                           widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2', 'placeholder': 'Add new task'}))