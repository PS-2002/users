from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = {'user_type',
                  'first_name',
                   'last_name', 
                   'profile_picture',
                   'username',
                   'email',
                   'address_line1',
                   'city',
                   'state',
                   'pincode'}
        
    def check_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('passwords do not match')
        return self.cleaned_data['password2']
    

class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)