from django import forms


class PasswordForm(forms.Form):
    tamanho = forms.IntegerField(label='Tamanho da senha', min_value=1, max_value=74)
