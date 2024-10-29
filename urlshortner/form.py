from django import forms
from .models import ShortenedUrl


class URLFORMS(forms.ModelForm):
    class Meta:
        model = ShortenedUrl
        fields = ['original_url']
        