from django.shortcuts import render
from .forms import PasswordForm
import random


def validar_tamanho_chave(digite_tamanho, tamanho_maximo):
    """
    Função que valida o tamanho da chave de criptografia
    """
    while not digite_tamanho.isdigit():
        digite_tamanho = input(
            "Digite apenas números, sem letras e caracteres especiais: "
        )

    digite_tamanho = int(digite_tamanho)

    if digite_tamanho > tamanho_maximo:
        print(
            f"Sua chave de criptografia não pode conter mais do que {tamanho_maximo} caracteres"
        )
        return None
    else:
        return digite_tamanho


def gerar_chave_criptografia(tamanho):
    """
    Função que gera a chave de criptografia
    """
    chars = "01234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?@#$%^&*()=+][}{;:"
    chave = "".join(random.sample(chars, tamanho))
    return chave


def generate_password(request):
    tamanho_maximo_chave = 74

    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            tamanho_chave = form.cleaned_data['tamanho']
            chave = gerar_chave_criptografia(tamanho_chave)
            return render(request, 'resultado.html', {'chave': chave})
    else:
        form = PasswordForm()

    return render(request, 'gerador.html', {'form': form})


def home(request):
    return render(request, 'home.html')
