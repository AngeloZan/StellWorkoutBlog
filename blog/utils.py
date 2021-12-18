from decimal import Context
from account.models import Account
from django.core.mail import send_mass_mail, send_mail, get_connection, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from account.utils import generate_token
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags

def posts_matrix(posts):
    # recebe uma lista de posts e organiza-os em uma matriz 3x3
    mtx = [ [], ]

    for post in posts:
        if len(mtx[-1]) < 3:
            mtx[-1].append(post)
        else:
            mtx.append([post])

    return mtx


def send_mass_html_mail(datatuple, fail_silently=False, user=None, password=None, 
                        connection=None):
    """
    FUNCAO AUXILIAR PARA EMAIL_NOTIFICATION
    Given a datatuple of (subject, text_content, html_content, from_email,
    recipient_list), sends each message to each recipient list. Returns the
    number of emails sent.

    If from_email is None, the DEFAULT_FROM_EMAIL setting is used.
    If auth_user and auth_password are set, they're used to log in.
    If auth_user is None, the EMAIL_HOST_USER setting is used.
    If auth_password is None, the EMAIL_HOST_PASSWORD setting is used.

    """
    connection = connection or get_connection(
        username=user, password=password, fail_silently=fail_silently)
    messages = []
    for subject, text, html, from_email, recipient in datatuple:
        message = EmailMultiAlternatives(subject, text, from_email, recipient)
        message.attach_alternative(html, 'text/html')
        messages.append(message)
    return connection.send_messages(messages)


def email_notification(post, domain):
    # manda email com notificação de novo post para todas as pessoas com email verificado
    subject = 'Novo Post: {}'.format(post.title)
    sender = settings.POST_NOTIFICATION_EMAIL
    destinatarios = Account.objects.filter(subscriber=True)

    mails = tuple()
    

    for user in destinatarios:
        # criando uma mensagem para cada user subscriber
        
        context = {
            'post': post,
            'domain': domain,
            'user': user,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)
        }

        msg_html = render_to_string('blog/novo_post_email.html', context)
        msg_plain = strip_tags(msg_html)
        
        mails += ((subject, msg_plain, msg_html, sender, [user.email]),)

    send_mass_html_mail(mails, fail_silently=True)
