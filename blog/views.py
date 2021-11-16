from django.forms.widgets import PasswordInput
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CreatePostForm

def posts_view(request):
    context = {}

    user = request.user

    if not user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'blog/posts.html', context)

def create_post_view(request):
    context = {}

    user = request.user

    if not user.is_admin:
        return redirect('home')

    if request.POST:
        form_novo_post = CreatePostForm(request.POST, request.FILES)
    else:    
        form_novo_post = CreatePostForm()

    if form_novo_post.is_valid():
        obj = form_novo_post.save(commit=False)
        obj.user = user
        obj.save()
        messages.success(request, f'O post foi enviado com sucesso!')
        return redirect('home')

    context['form_novo_post'] = form_novo_post

    return render(request, 'blog/novo_post.html', context)
    

