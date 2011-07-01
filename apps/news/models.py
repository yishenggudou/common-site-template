# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from pytils.translit import translify


class Category(models.Model):
    '''News category'''
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    slug = models.SlugField()
    pic = models.ImageField(upload_to="news/category", blank=True)

    class Meta:
        verbose_name = "Categories"
        verbose_name_plural = "Category"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(translify(self.name))
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])
    
    def __unicode__(self):
        return self.title
    

class NewsPost(models.Model):
    '''News
    pic - small picture for thumbnails
    is_draft - show or not (like wordpress draft posts)
    '''
    title = models.CharField(max_length=160)
    description = models.CharField(max_length=255, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    content = models.TextField(blank=True)
    category = models.ForeignKey(Category)
    pic = models.ImageField(upload_to="news/", blank=True)

    is_draft = models.BooleanField(blank=True, default=False)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(translify(self.name))
        super(NewsPost, self).save(*args, **kwargs)

    def get_category_slug(self):
        return self.category.slug

    def get_category(self):
        return self.category

    def get_absolute_url(self):
        return reverse('news_post', args=[self.get_category_slug, self.slug])

    def __unicode__(self):
        return self.title        
        
