from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Book(models.Model):
    title = models.CharField(
        max_length=255
    )

    author = models.CharField(
        max_length=255
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    modified_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')


class Reader(models.Model):
    first_name = models.CharField(
        max_length=30
    )

    last_name = models.CharField(
        max_length=30
    )

    books = models.ManyToManyField(
        to=Book,
        related_name='readers',
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    modified_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = _('Reader')
        verbose_name_plural = _('Readers')
