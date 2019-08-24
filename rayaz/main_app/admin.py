from django.contrib import admin
from .models import Profile
from .models import Restraunt, Review, Bookmark
from django import forms

class RestrauntForm(forms.ModelForm ):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Restraunt
        fields = '__all__'

class RestrauntAdmin(admin.ModelAdmin):
    form = RestrauntForm

admin.site.register(Profile)
admin.site.register(Restraunt,RestrauntAdmin)
admin.site.register(Review)
admin.site.register(Bookmark)
