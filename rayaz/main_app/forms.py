from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Review


class ProfileForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Profile
        fields = ("image",)

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30,required=True,widget=forms.TextInput(attrs={'style':'outline: 0;'}))
    first_name = forms.CharField(max_length=30, required=False,widget=forms.TextInput(attrs={'style':'outline: 0;'}))
    last_name = forms.CharField(max_length=30, required=False,widget=forms.TextInput(attrs={'style':'outline: 0;'}))
    email = forms.EmailField(max_length=254,required=True,widget=forms.TextInput(attrs={'style':'outline:0;'}))
    password1 = forms.CharField(max_length=254,required=True,widget=forms.PasswordInput(attrs={'style':'outline: 0;'}),label="Password:")
    password2 = forms.CharField(max_length=254,required=True,widget=forms.PasswordInput(attrs={'style':'outline: 0;'}),label='Confirm Password')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True,label='Name')
    contact_email = forms.EmailField(required=True,label='Email')
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,label="Message")

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title','text')
