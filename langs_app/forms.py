from django import forms
from .models import Word, Voice, FullData


class AddWordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = "__all__"

class AddVoiceForm(forms.ModelForm):
    class Meta:
        model = Voice
        fields = "__all__"

class AddFullDataForm(forms.ModelForm):
    class Meta:
        model = FullData
        fields = "__all__"