from django import forms
from .models import JapWord, VerbConjugation


class JapWordForm(forms.ModelForm):
    class Meta:
        model = JapWord
        fields = ['text']
        labels = {'text': ''}


class VerbConjugationForm(forms.ModelForm):
    class Meta:
        model = VerbConjugation
        fields = ['polite',
                  'te_form',
                  'past',
                  'negative',
                  'imperative',
                  'volitional',
                  'conditional',
                  'potential',
                  'passive',
                  'causative']
        labels = {'polite': 'ます形',
                  'te_form': 'て形',
                  'past': 'た形',
                  'negative': '未然形',
                  'imperative': '命令形',
                  'volitional': '意志形',
                  'conditional': 'ば形',
                  'potential': '可能形',
                  'passive': '被動形',
                  'causative': '使役形'}
