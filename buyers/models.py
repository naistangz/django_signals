from django.db import models
from django.contrib.auth.models import User
import uuid

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    from_signal = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if self.code == "":
            self.code = str(uuid.uuid4()).replace("-", "").upper()[:10]
        return super().save(*args, **kwargs)