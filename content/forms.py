from django.forms import ModelForm
from .models import Content


class ContactForm(ModelForm):
    class Meta:
        model = Content
        fields = '__all__'