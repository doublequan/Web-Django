from __future__ import unicode_literals

from django.db import models

# Create your models here.


class SiteNotice(models.Model):
    notice = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.notice + " : " + self.link