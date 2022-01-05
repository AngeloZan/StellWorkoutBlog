from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from django.conf import settings
from django.core.mail import send_mail

from StellWorkoutBlog.settings import AJUDA_EMAIL_RECEIVER

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.confirmed) + six.text_type(user.subscriber) + user.password
        )

generate_token = TokenGenerator()


def ajuda_email(nome, email, mensagem):
    subject = 'Ajuda solicitada por {}'.format(nome)
    sender = settings.AJUDA_EMAIL_SENDER
    destinatarios = [AJUDA_EMAIL_RECEIVER]

    message = '''Nome: {nome}\nContato: {email}\nMensagem:\n\n{mensagem}\n'''.format(nome=nome, email=email, mensagem=mensagem)

    send_mail(subject, message, sender, destinatarios, fail_silently=True)
