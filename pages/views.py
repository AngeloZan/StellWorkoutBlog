from django.shortcuts import render, redirect

def home_view(request):
    context = {}

    user = request.user

    if not user.is_authenticated:
        return render(request, 'pages/home.html', context)
    else:
        return render(request, 'pages/home.html', context) # por enquanto retornando para a mesma pag

        