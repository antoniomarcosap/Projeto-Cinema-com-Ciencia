from django.db import models


class Base(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class Member(Base):
    name = models.CharField(
        max_length=60,
        unique=True,
    )

    title = models.CharField(
        max_length=30,
    )

    bio = models.CharField(
        max_length=255,
        blank=True,
    )

    photo = models.ImageField(
        upload_to=('photo/%Y/%m/%d'),
    )

    lattes = models.URLField(
        unique=True,
    )

    class Meta:
        ordering = ('-created'),

    def __str__(self):
        return self.name
