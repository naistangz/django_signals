from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Car

import uuid


@receiver(pre_save, sender=Car)
def pre_save_create_code(sender, instance, **kwargs):
    if instance.code == "":
        instance.code = str(uuid.uuid4()).replace("-", "").upper()[:10]
