from django import forms

class StartForm(forms.Form):
    GAME_TYPES = [
        ('sumas', 'Sumas'),
        ('restas', 'Restas'),
        ('multiplicacion', 'Multiplicación'),
        ('division', 'División'),
    ]
    game_type = forms.ChoiceField(choices=GAME_TYPES)
    level = forms.IntegerField(min_value=1, max_value=5, initial=1)
    total = forms.IntegerField(min_value=5, max_value=20, initial=10)
