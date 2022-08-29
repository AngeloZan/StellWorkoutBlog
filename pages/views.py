from django.shortcuts import render, redirect
from django.contrib import messages

def home_view(request):
    context = {}

    user = request.user
    context['user'] = user

    if not user.is_authenticated:
        return render(request, 'pages/home.html', context)
    else:
        return redirect('posts')


def sobre_view(request):
    context = {}

    return render(request, 'pages/construction.html', context)


def stell_wear_view(request):
    context = {}

    return render(request, 'pages/construction.html', context)


def patrocinio_view(request):
    context = {}

    return render(request, 'pages/construction.html', context)


def faq_view(request):
    context = {}

    return render(request, 'pages/construction.html', context)


def termos_e_condicoes_view(request):
    context = {}

    return render(request, 'pages/construction.html', context)


def politica_de_privacidade_view(request):
    context = {}

    return render(request, 'pages/construction.html', context)

