# This is not actually my code
# You can check https://www.youtube.com/playlist?list=PLgCYzUzKIBE_dil025VAJnDjNZHHHR9mW
# I used this course to build my account app

from decimal import Context
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm, PasswordChangeFormCustom
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from .models import Account
from django.contrib import messages
import os
from django.utils.html import strip_tags
from django.contrib.auth.forms import SetPasswordForm
from django.http.response import HttpResponse

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)

            if (not settings.DEBUG) or settings.TEST_EMAIL:
                # enviando email de confirmacao
                user.save()

                current_site = get_current_site(request)
                email_subject = 'Confirme o seu endereço de E-mail'
                message = render_to_string('account/activate.html',
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': generate_token.make_token(user)
                })

                email_message = EmailMessage(
                    email_subject,
                    message,
                    settings.CONFIRMATION_FROM_EMAIL,
                    [email]
                )

                email_message.send()

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
    # apesar do nome, coloca o usuario na lista de emails
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except Exception as identifier:
        user = None
    
    if user is not None and generate_token.check_token(user, token):
        user.confirmed = True
        user.subscriber = True
        user.save()
        messages.success(request, f'Email verificado com sucesso!')
        return redirect('home')

    return render(request, 'account/activate_failed.html', status=401)


def my_data_view(request):
    context = {}

    user = request.user

    if not user.is_authenticated:
        return redirect('login')
     
    if request.POST:
        u_form = AccountUpdateForm(request.POST, instance=user)
    else:
        u_form = AccountUpdateForm(instance=user)

    if u_form.is_valid():
        u_form.save()
        messages.success(request, f'Sua conta foi atualizada!')
        return redirect('home')
    
    context['user'] = user
    context['u_form'] = u_form

    return render(request, 'account/my_data.html', context)


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
            return redirect('home')

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
                messages.info(request, 'Sua conta foi excluída, até a próxima!')
                return redirect('home')

    else:
        form = AccountAuthenticationForm()

    context['del_user_form'] = form
    return render(request, 'account/del_user.html', context)


def password_reset_form_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        email = request.POST.get('email')
        context['email'] = email
        registered_user = Account.objects.filter(email=email)

        if registered_user:
            if registered_user[0].confirmed:
                # mandar email
                if (not settings.DEBUG) or settings.TEST_EMAIL:
                    current_site = get_current_site(request)
                    email_subject = 'Recuperação de senha'
                    msg_html = render_to_string('account/password_reset_email.html',
                    {
                        'user': registered_user[0],
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(registered_user[0].pk)),
                        'token': generate_token.make_token(registered_user[0])
                    })
                    msg_plain = strip_tags(msg_html)

                    send_mail(email_subject, msg_plain, settings.RESET_PASSWORD_EMAIL, [email], html_message=msg_html)

                messages.success(request, f'Enviamos um email para {email}, verifique também a sua caixa de spam.')
                return redirect('home')
            else:
                # redirecionar e informar que o email não é verificado
                context['user_exists'] = True
                return render(request, 'account/password_reset_form_failed.html', context)

        else:
            # redirecionar e informar que o email não foi encontrado no BD
            context['user_exists'] = False
            return render(request, 'account/password_reset_form_failed.html', context)

    # get request
    return render(request, 'account/password_reset_form.html')

def password_reset_new_pass_form(request, uidb64, token):
    # o link para recuperacao de senha direciona para essa funcao
    context = {}
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except Exception as identifier:
        user = None
    
    if user is not None and generate_token.check_token(user, token):
        if request.POST:
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, f'Senha redefinida com sucesso!')
                login(request, user)
                return redirect('home')
        else:
            form = SetPasswordForm(user=user)

        context['form'] = form
        return render(request, 'account/password_reset_new_pass.html', context)

    return render(request, 'account/password_reset_fail.html', status=401)


def toggle_theme_view(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('home')
    else:
        user.dark_mode = not user.dark_mode
        user.save()

    return HttpResponse('')
