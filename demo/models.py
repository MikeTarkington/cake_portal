from django.db import models
# from cake_portal.models import GoogleCal

class Demoer(models.Model):
     # tie to user model through db association and remove redundant attributes like name or lead
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
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
