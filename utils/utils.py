#! -*- coding: utf-8 -*-
from django.conf import settings

import smtplib
import string
from random import choice
from django.core.mail import EmailMultiAlternatives


def send_email(html_content,to):
    subject, from_email = 'Kullanici Kaydi', 'akagunduzebru8@gmail.com'
    text_content = 'mesaj icerigi'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def generate_url_id():
    url_id = ''.join([choice(string.letters + string.digits) for i in range(20)])
    #return HttpResponse(url_id)
    return url_id
