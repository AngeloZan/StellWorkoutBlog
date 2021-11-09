from django.shortcuts import render, redirect

def posts_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'blog/posts.html', context)
