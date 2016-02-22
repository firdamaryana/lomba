from django import forms
from .models import Summarization
from django.contrib.auth.models import User
from blog.models import UserProfile

class SummarizationForm(forms.ModelForm):
	# An inline class to provide additional information on the form.
    PILIHAN=(
            (1,1),
            (2,2),
            (3,3),
            (4,4),
            (5,5),
            )
    jumlah = forms.ChoiceField(choices=PILIHAN)
    text = forms.CharField(widget=forms.Textarea, error_messages={'required': 'Teks Tidak Boleh Kosong!'})
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Summarization
        fields = ('text',)

class UserForm(forms.Form):

    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

#    class Meta:
 #       model = User
  #      fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
