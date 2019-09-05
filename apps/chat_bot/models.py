from django.db import models

from apps.core.models import AbstractBaseModel
from apps.core.utils import generate_unique_id


class Threads(AbstractBaseModel):
    user_name = models.CharField(max_length=42, blank=False, null=False)
    id = models.CharField(primary_key=True, max_length=8)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_unique_id(self.user_name)
        super(Threads, self).save(*args, **kwargs)

    @property
    def get_thread_id(self):
        return self.id


    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name_plural = 'Threads'
