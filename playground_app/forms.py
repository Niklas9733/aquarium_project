from django import forms
from .models import Character

# Formular zur Aktualisierung des Ortes (lieu) eines Charakters
class MoveForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('lieu',)  # Nur das Feld 'lieu' soll im Formular erscheinen
