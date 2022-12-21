from .models import Computer
from django import forms

# form for computer information
class CreateModel(forms.ModelForm):
    class Meta:
        model=Computer
        fields='__all__'