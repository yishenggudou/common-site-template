# -*- coding: utf-8 -*-
from django.db import models
from tinymce import models as tinymce_models


class SidebarLink(models.Model):
    '''Sidebar link control'''
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)


class ContentBlock(models.Model):
    '''Content blocks which i can edit from admin interface'''
    block_id = models.CharField(max_length=160, unique=True,
                                help_text="uniq block id (about_us, contatcs etc)")
    title = models.CharField(max_length=160, blank=True, help_text="title")
    #content = tinymce_models.HTMLField(blank=True, help_text="content")
    content = models.TextField(blank=True, help_text="content")
