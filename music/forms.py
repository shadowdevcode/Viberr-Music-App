from django.contrib.auth.models import User
from django import forms
from .models import Song

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Display password

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']