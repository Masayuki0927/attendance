from django import forms
from .models import Attendance
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser

class AttendForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = ('attend', )

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='必須 有効なメールアドレスを入力してください。',
        label='Eメールアドレス'
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', )