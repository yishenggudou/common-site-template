# -*- coding: utf-8 -*-
from django.db import models


class SidebarLink(models.Model):
    '''Sidebar link control'''
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)


class ContentBlock(models.Model):
    '''Content blocks which i can edit from admin interface'''
    block_id = models.CharField(max_length=160, unique=True,
                                help_text="uniq block id (about_us, contatcs etc)")
    title = models.CharField(max_length=160, blank=True, help_text="title")
    content = models.TextField(blank=True, help_text="content")


class Services(models.Model):
    """ Services """
    title = models.CharField(max_length=160)
    desc = models.CharField(max_length=255, blank=True)

    slug = models.SlugField()
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
