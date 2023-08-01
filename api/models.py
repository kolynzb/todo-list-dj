from django.utils.translation import gettext as _
from utils.models import TimeStampedUUIDModel
from django.db import models


# Create your models here.
class Todo(TimeStampedUUIDModel):
    """
    A model representing a Todo item.

    This model stores information about a Todo item, including its title, text,
    completion status, creation date, and last update date.
    """

    title = models.CharField(verbose_name=_("Todo Title"),max_length=225)
    text = models.TextField(verbose_name=_("Todo Text"),max_length=225)
    completed = models.BooleanField(default=False, help_text=_('Designates whether Job Post is a Draft.'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str(self):
        return self.title