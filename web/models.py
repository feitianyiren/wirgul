#! -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext
from django.conf import settings

from wirgul.utils.messages import WEB_MODEL_EMAIL, WEB_MODEL_MIDDLE_NAME, WEB_MODEL_SURNAME, WEB_MODEL_YOURNAME, WEB_MODEL_FACULTY, WEB_MODEL_DEPARTMENT

class Faculty(models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return u'%s' % (self.name)

class Department(models.Model):
    name = models.CharField(max_length=150)
    faculty = models.ForeignKey(Faculty)

    def __unicode__(self):
        return u'%s' % (self.name)

class UrlId(models.Model):
    url_id = models.CharField(max_length=100)

class FirstTimeUserSecret(models.Model):
    passwd_change_time = models.DateTimeField(auto_now=True)

class PasswordChange(models.Model):
    email = models.EmailField(verbose_name=gettext(WEB_MODEL_EMAIL))
    url = models.CharField(max_length=100)
    url_create_time = models.DateTimeField()
    status = models.BooleanField(default=False)

class FirstTimeUser(models.Model):
    name = models.CharField(verbose_name=gettext(WEB_MODEL_YOURNAME),max_length=50)
    middle_name = models.CharField(verbose_name=gettext(WEB_MODEL_MIDDLE_NAME),max_length=50, null=True, blank=True)
    surname = models.CharField(verbose_name=gettext(WEB_MODEL_SURNAME),max_length=100)
    faculty = models.ForeignKey(Faculty,verbose_name=gettext(WEB_MODEL_FACULTY))
    department = models.ForeignKey(Department,verbose_name=gettext(WEB_MODEL_DEPARTMENT))
    email = models.EmailField(unique=True,verbose_name=gettext(WEB_MODEL_EMAIL))
    application = models.DateTimeField(auto_now=True)
    url = models.ForeignKey(UrlId, blank=True, null=True)
    secret = models.ForeignKey(FirstTimeUserSecret, blank=True,null=True)

class GuestUser(models.Model):
    name = models.CharField(verbose_name=gettext('İsminiz:'),max_length=50)
    middle_name = models.CharField(verbose_name=gettext('Orta Adiniz:'),max_length=50, null=True, blank=True)
    surname = models.CharField(verbose_name=gettext('Soyadiniz:'),max_length=100)
    guest_user_email = models.EmailField(verbose_name=gettext('Mail Adresiniz'))
    email = models.EmailField(verbose_name=gettext('Misafiri Oldugunuz Kişinin mail adresi:'))
    url = models.CharField(max_length=100)
    TIME_CHOICES = (
        (1, 'SAAT'),
        (2, 'GUN'),
        (3, 'HAFTA'),
        )
    type = models.CharField(blank=True,null=True,choices=TIME_CHOICES,default=1,max_length=10,verbose_name=gettext("Saat Gün ya da Hafta Seçiniz"))
    time_duration = models.CharField(blank=True,null=True,choices=settings.TIME_DURATION_CHOICES,verbose_name="Süreyi Seçiniz",max_length=10)
    start = models.DateTimeField(auto_now=True)
    guest_user_phone = models.IntegerField("Telefon Numaranız :",max_length=10)
