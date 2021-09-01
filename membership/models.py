import uuid

from django.db import models
from django.utils import timezone


class User(models.Model):
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        verbose_name='User ID(PK)'
    )

    name = models.CharField(
        max_length=256
    )

    birthday = models.DateTimeField(
        default=timezone.now
    )

    username = models.CharField(
        max_length=128
    )

    password_hash = models.CharField(
         max_length=128
    )


class Billing(models.Model):
    plan_name = models.CharField(
        max_length=64
    )


class BillingPlan(models.Model):
    start_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Start Date'
    )

    end_date = models.DateTimeField(
        auto_now=True,
        verbose_name='End Date'
    )

    billing = models.ForeignKey(
        'Billing',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
