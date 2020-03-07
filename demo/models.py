from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from cake_portal.models import GoogleCal

class Demoer(models.Model):
    email = models.EmailField(blank=False, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    US_EAST = "US-EAST"
    US_WEST = "US-WEST"
    EMEA = "EMEA"
    APAC = "APAC"
    REGION_CHOICES = (
        (US_EAST, 'US-East'),
        (US_WEST, 'US-West'),
        (EMEA, 'EMEA'),
        (APAC, 'APAC'),
    )
    region = models.CharField(choices=REGION_CHOICES, max_length=30)
    lead = models.CharField(max_length=50)
    need_shadow = models.BooleanField()
    three_pillar = models.BooleanField()
    apm = models.BooleanField()
    logs = models.BooleanField()
    custom_metrics = models.BooleanField()
    notes = models.CharField(max_length=250)
    preferred_topic = models.CharField(max_length=50, null=True, blank=True)
    LOW_MRR = 1400
    MED_MRR = 2500
    HIGH_MRR = 3500
    MAX_MRR = 5000
    MRR_CHOICES = (
        (LOW_MRR, '1400'),
        (MED_MRR, '2500'),
        (HIGH_MRR, '3500'),
        (MAX_MRR, '5000'),
    )
    max_mrr = models.IntegerField(choices=MRR_CHOICES)

    @staticmethod
    def demoer_by_mrr(mrr):
        mrr_demoers = Demoer.objects.filter(max_mrr__lte=mrr)
        return mrr_demoers

    @staticmethod
    def demoer_by_region(region):
        region_demoers = Demoer.objects.filter(region__exact=region)
        return region_demoers

    @staticmethod
    def available_demoers(datetime, region, mrr):
        return "who's available"

    # def __str__(self):
    #     return self.first_name
