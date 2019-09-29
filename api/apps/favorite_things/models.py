from django.db import models
from django.core.validators import (
    MinLengthValidator,
    MinValueValidator,
    MaxValueValidator
)


class Categories(models.Model):

    name = models.CharField(
        max_length=10,
        unique=True,
        validators=[MinLengthValidator(3)]
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.name


class FavoriteThings(models.Model):

    title = models.CharField(max_length=60)
    description = models.CharField(
        max_length=500,
        blank=True,
        validators=[MinLengthValidator(10)]
    )
    metadata = models.TextField(default=[], blank=True)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    rank = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5000)
        ]
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class AuditLog(models.Model):
    title = models.CharField(max_length=60)
    action = models.CharField(max_length=16)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title
