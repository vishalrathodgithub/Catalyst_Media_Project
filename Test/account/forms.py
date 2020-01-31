from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    Date_Of_Birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date','format':'%D%M%Y'}))
    class Meta:
        model = User
        fields = ['Name','Email','Password','Date_Of_Birth','Mobile_Number']

class UserLoginForm(forms.Form):
    Name = forms.CharField(max_length=45)
    Password = forms.CharField(widget=forms.PasswordInput)

class UserUpdateForm(forms.ModelForm):
    Date_Of_Birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date','format':'%D%M%Y'}))
    class Meta:
        model = User
        fields = ['Name','Email','Date_Of_Birth','Mobile_Number']