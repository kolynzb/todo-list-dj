"""
utils/models.py

This module contains abstract base models for common functionalities used across django apps.

"""
import uuid

from django.db import models

# Create your models here.

class UUIDModel(models.Model):
    """
    An abstract base model with a UUID primary key.

    This model provides a UUID (Universally Unique Identifier) as the primary key.
    The `id` field is automatically generated using `uuid.uuid4()` and is set as the
    primary key, making each record have a unique identifier.

    Attributes:
        id (uuid.UUID): The UUID primary key for the model.
    """
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True

class TimeStampedUUIDModel(models.Model):
    """
    An abstract base model with a UUID primary key and timestamp fields.

    This model extends the `UUIDModel` and provides additional timestamp fields:
    - `created_at`: The date and time when the record was created.
    - `updated_at`: The date and time when the record was last updated.

    Attributes:
        id (uuid.UUID): The UUID primary key for the model.
        created_at (datetime): The date and time when the record was created (auto-generated).
        updated_at (datetime): The date and time when the record was last updated (auto-updated).
    """

    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

