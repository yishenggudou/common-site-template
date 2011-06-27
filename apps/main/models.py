from django.db import models


class Services(models.Model):
    """ Services """
    title = models.CharField(max_length=160)
    desc = models.CharField(max_length=255, blank=True)

    slug = models.SlugField()
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
