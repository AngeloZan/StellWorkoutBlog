"""StellWorkoutBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# mudando o titulo da pagina admin
admin.site.site_header = 'Administração StellWorkout'

from pages.views import (
    home_view,
)

from account.views import (
    password_reset_form_view,
    registration_view,
    login_view,
    logout_view,
    my_data_view,
    activate_account_view,
    change_password_view,
    del_user_view,
    password_reset_form_view,
    password_reset_new_pass_form,
    toggle_theme_view,
    profile_view,
)

from blog.views import (
    posts_view,
    create_post_view,
    search_posts_view,
    unsubscribe_view,
    favourite_post_view,
    favourite_posts_view,
    posts_categoria_view,
    feedback_view,
)

urlpatterns = [
    path('5t3llw0rk0ut4dm1n15tr4c40/', admin.site.urls, name='admin'),
    path('', home_view, name='home'),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('dados/', my_data_view, name="my_data"),
    path('excluir-conta/', del_user_view, name='del_user'),
    path('activate/<uidb64>/<token>', activate_account_view, name='activate'),
    path('alterar-senha/', change_password_view, name='change_password'),
    path('posts/', posts_view, name='posts'),
    path('novo-post/', create_post_view, name='novo_post'),
    path('search-posts/', search_posts_view, name='search_posts'),
    path('unsubscribe/<uidb64>/<token>', unsubscribe_view, name='unsubscribe'),
    path('mudar-senha', password_reset_form_view, name='password_reset'),
    path('mudar-senha-redefinir/<uidb64>/<token>', password_reset_new_pass_form, name='password_reset_new_pass'),
    path('<id>/favourite-post/', favourite_post_view, name='favourite_post'),
    path('favourite-posts/', favourite_posts_view, name='favourite_posts'),
    path('posts/<categoria>', posts_categoria_view, name='posts_categoria'),
    path('toggle-theme/', toggle_theme_view, name='toggle_theme'),
    path('feedback/', feedback_view, name='feedback'),
    path('perfil/', profile_view, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
