from django.contrib.auth.forms import UserCreationForm
from .models import User, Review
from django import forms
 
class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email','first_name', 'last_name',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError( "Email já cadastrado.")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            match = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Usuário já cadastrado.")

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('note', 'text')