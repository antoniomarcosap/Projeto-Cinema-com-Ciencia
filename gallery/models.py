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


class Gallery(Base):
    title = models.CharField(
        max_length=150,
        unique=True,
    )

    image = models.ImageField(
        upload_to=('gallery/%Y/%m/%d'),
    )

    class Meta:
        ordering = ('created',)
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return self.title
