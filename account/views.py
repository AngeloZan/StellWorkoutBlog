# This is not actually my code
# You can check https://www.youtube.com/playlist?list=PLgCYzUzKIBE_dil025VAJnDjNZHHHR9mW
# I used this course to build my account app

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm, ProfileUpdateForm, PasswordChangeFormCustom
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Account
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
import os

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)

            user = Account.objects.get(email=email)

            if not settings.DEBUG:
                user.is_active = False
                user.save()

                current_site = get_current_site(request)
                email_subject = 'Ative a sua conta'
                message = render_to_string('account/activate.html',
                {
                    'user': account,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(account.pk)),
                    'token': generate_token.make_token(account)
                })

                email_message = EmailMessage(
                    email_subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email]
                )

                email_message.send()
            else:
                login(request, account)

            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm
        context['registration_form'] = form

    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'account/login.html', context)


def activate_account_view(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except Exception as identifier:
        user = None
    
    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')

    return render(request, 'account/activate_failed.html', status=401)


def profile_view(request):
    context = {}

    user = request.user

    if not user.is_authenticated:
        return redirect('login')

    user_old_pic_file = user.profile.image.path
    
    
    if request.POST:
        u_form = AccountUpdateForm(request.POST, instance=user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)
    else:
        u_form = AccountUpdateForm(instance=user)
        p_form = ProfileUpdateForm(instance=user.profile)

    if u_form.is_valid() and p_form.is_valid():

        if len(request.FILES) != 0:
            if not user_old_pic_file.endswith('media/default.jpg'):
                os.remove(user_old_pic_file)

        u_form.save()
        p_form.save()
        messages.success(request, f'Sua conta foi atualizada!')
        return redirect('profile')
    
    context['user'] = user
    context['u_form'] = u_form
    context['p_form'] = p_form

    return render(request, 'account/profile.html', context)


def metas_view(request):
    context = {}

    user = request.user

    if not user.is_authenticated:
        return redirect('login')
    
    if request.POST:
        return redirect('home') # temporário
    else:
        return render(request, 'account/metas.html', context)


def change_password_view(request):

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = PasswordChangeFormCustom(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            list(messages.get_messages(request))
            messages.success(request, 'Sua senha foi atualizada com sucesso!')
            return redirect('profile')

    else:
        form = PasswordChangeFormCustom(request.user)
    return render(request, 'account/change_password.html', {
        'form': form
    })

def del_user_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    user_old_pic_file = user.profile.image.path

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = user.email
            password = request.POST['password']
            u = authenticate(email=email, password=password)

            if u:
                if not user_old_pic_file.endswith('media/default.jpg'):
                    os.remove(user_old_pic_file)
                u.delete()
                messages.success(request, 'Sua conta foi excluída, até a próxima!')
                return redirect('home')

    else:
        form = AccountAuthenticationForm(initial={'email': user.email})

    context['del_user_form'] = form
    return render(request, 'account/del_user.html', context)