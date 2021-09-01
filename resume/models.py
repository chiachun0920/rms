import uuid

from django.db import models
from django.utils import timezone


class Resume(models.Model):
    name = models.CharField(
        max_length=256
    )

    user = models.ForeignKey(
        'membership.User',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )


class ResumeTemplate(models.Model):
    template_name = models.CharField(
        max_length=256
    )

    resume = models.ForeignKey(
        'Resume',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )


class JobExperience(models.Model):
    start_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Start Date'
    )

    end_date = models.DateTimeField(
        auto_now=True,
        verbose_name='End Date'
    )

    company_name = models.CharField(
        max_length=128
    )

    user = models.ForeignKey(
        'membership.User',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
