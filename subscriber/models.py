# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Subscriber(models.Model):
    def __unicode__(self):
           return self.name
    contact_home_email = models.CharField(max_length=100)
    contact_home_phone = models.CharField(max_length=100)
    contact_work_email = models.CharField(max_length=100)
    contact_work_phone = models.CharField(max_length=100)
    credit_address = models.CharField(max_length=100)
    imsi = models.IntegerField
    msisdn = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    ssn = models.CharField(max_length=11)
