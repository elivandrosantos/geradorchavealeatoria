from django import forms


class PasswordForm(forms.Form):
    tamanho = forms.IntegerField(label='Digite tamanho de 1 á 74:', min_value=1, max_value=74)
