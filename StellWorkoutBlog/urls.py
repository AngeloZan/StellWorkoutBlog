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

from pages.views import (
    home_view,
)

from account.views import (
    registration_view,
    login_view,
    logout_view,
    profile_view,
    activate_account_view,
    metas_view,
    change_password_view,
    del_user_view,
)

from blog.views import (
    posts_view,
)

urlpatterns = [
    path('5t3llw0rk0ut4dm1n15tr4c40/', admin.site.urls, name='admin'),
    path('', home_view, name='home'),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('perfil/', profile_view, name="profile"),
    path('metas/', metas_view, name='metas'),
    path('excluir-conta/', del_user_view, name='del_user'),
    path('activate/<uidb64>/<token>', activate_account_view, name='activate'),
    path('alterar-senha/', change_password_view, name='change_password'),
    path('posts/', posts_view, name='posts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
