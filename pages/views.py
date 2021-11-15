from django.shortcuts import render, redirect
from django.contrib import messages

def home_view(request):
    context = {}

    user = request.user
    context['user'] = user

    if not user.is_authenticated:
        return render(request, 'pages/home.html', context)
    else:
        return render(request, 'blog/posts.html', context)

        