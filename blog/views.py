from django.conf import settings
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from account.models import Account
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .utils import generate_token
from django.http import Http404

from .utils import posts_matrix, email_notification
from .models import Post, CATEGORIAS_POSTS
from .forms import CreatePostForm

def posts_view(request):
    context = {}

    user = request.user

    if not user.is_authenticated:
        return redirect('home')
    else:
        posts = Post.objects.order_by('-date_added')
        favourite_posts = user.favourite.all()
        context['todos_posts'] = posts
        context['categorias'] = []
        context['favourite_posts'] = favourite_posts

        for categoria, verbose_name in CATEGORIAS_POSTS:
            if categoria != 'nenhuma':
                posts_categoria = posts.filter(category=categoria)
                if posts_categoria:
                    context['categorias'].append((categoria, verbose_name, posts_categoria))
        
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

        if request.POST.get('notification') and ((not settings.DEBUG) or settings.TEST_EMAIL):
            domain = get_current_site(request)
            email_notification(obj, domain) # mandando email com notificação

        return redirect('home')

    context['form_novo_post'] = form_novo_post

    return render(request, 'blog/novo_post.html', context)
    

def search_posts_view(request):
    context = {}

    user = request.user

    if not user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        searched = request.POST.get('searched', False)
        context['searched'] = searched

        posts_title = Post.objects.filter(title__contains=searched)
        posts_intro = Post.objects.filter(intro__contains=searched)
        posts = posts_title | posts_intro
        num_posts = len(posts)
        posts_mtx = posts_matrix(posts)
        favourite_posts = user.favourite.all()
        context['posts_mtx'] = posts_mtx
        context['num_posts'] = num_posts
        context['favourite_posts'] = favourite_posts

        return render(request, 'blog/search_posts.html', context)
    else:
        return redirect('home')


def unsubscribe_view(request, uidb64, token):
    # remove um usuario da lista de emails
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except Exception as identifier:
        user = None
    
    if user is not None and generate_token.check_token(user, token):
        user.subscriber = False
        user.save()
        messages.info(request, f'Você não receberá mais emails.')
        return redirect('home')

    return render(request, 'blog/unsubscribe_failed.html', status=401)


def favourite_post_view(request, id):
    post = get_object_or_404(Post, id=id)
    if post.favourite.filter(id=request.user.id).exists():
        post.favourite.remove(request.user)
    else:
        post.favourite.add(request.user)

    return HttpResponse('')

def favourite_posts_view(request):
    context = {}

    user = request.user

    if not user.is_authenticated:
        return redirect('home')

    posts = user.favourite.all()
    posts_mtx = posts_matrix(posts)
    num_posts = len(posts)
    favourite_posts = user.favourite.all()
    context['favourite_posts'] = favourite_posts
    context['num_posts'] = num_posts
    context['posts_mtx'] = posts_mtx

    return render(request, 'blog/favourite_posts.html', context)


def posts_categoria_view(request, categoria):
    context = {}

    user = request.user

    if not user.is_authenticated:
        return redirect('home')
    else:
        if not categoria == 'todos':
            categoria_name = categoria.replace('-', '_')
            try:
                categoria_verbose = CATEGORIAS_POSTS[[name for name, verbose in CATEGORIAS_POSTS].index(categoria_name)][1]
            except:
                raise Http404

            posts = Post.objects.filter(category=categoria)
        else:
            categoria_name = 'todos'
            categoria_verbose = 'Todos'
            posts = Post.objects.all()
            
        favourite_posts = user.favourite.all()
        posts_mtx = posts_matrix(posts)
        context['posts_mtx'] = posts_mtx
        context['categoria_verbose'] = categoria_verbose
        context['favourite_posts'] = favourite_posts
        context['num_posts'] = len(posts)
        
        return render(request, 'blog/posts_categoria.html', context)


    


