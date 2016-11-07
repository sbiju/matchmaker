from __future__ import unicode_literals

from django.db import models, IntegrityError
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db.models.signals import post_save

GENDER_CHOICES = (('M', 'Male'),
                  ('F', 'Female'),
                  )
COUNTRY_CHOICES = (('us', 'United States'),
                  ('ca', 'Canada'),
                  )


def upload_location(instance, filename):
    return '%s, %s' %(instance.first_name, filename)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    first_name = models.CharField(max_length=80,blank=True, null=True)
    last_name = models.CharField(max_length=80, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    photo = models.FileField(upload_to=upload_location, blank=True, null=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True, null=True)
    country = models.CharField(default='us', choices=COUNTRY_CHOICES, max_length=150)
    zip_code = models.IntegerField(default='10001')
    masjid = models.CharField(max_length=200, default='Masjid At-Taqwa')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.user)

    # def get_absolute_url(self):
    #     return reverse('profiles:user_detail', kwargs={'pk': self.pk})


def post_save_user_model_reciever(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass

post_save.connect(post_save_user_model_reciever, sender=settings.AUTH_USER_MODEL)