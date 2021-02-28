from django.forms import ModelForm
from .models import Song
from crispy_forms.helper import FormHelper

class SongForm(ModelForm):
    helper = FormHelper()
    
    class Meta:
        model = Song
        fields = '__all__'