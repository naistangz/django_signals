from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Buyer


@receiver(post_save, sender=User)
def post_save_create_buyer(sender, instance, created, **kwargs):
    """
    Creates a buyer instance to sender (User)
    User is created
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    print('sender', sender)
    print('instance', instance)
    print('created', True)
    if created:
        Buyer.objects.create(user=instance)

