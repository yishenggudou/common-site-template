# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify

from pytils.translit import translify


class Category(models.Model):
    '''News category'''
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True)
    slug = models.SlugField()
    pic = models.ImageField(upload_to="news/category", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(translify(self.name))
        super(Category, self).save(*args, **kwargs)

    #def get_absolute_url(self):
    #    return reverse('category_details', args=[self.pk, self.slug])
    
    def __unicode__(self):
        return self.title
    

class NewsPost(models.Model):
    '''News'''
    title = models.CharField(max_length=160)
    description = models.CharField(max_length=255, blank=True)
    pub_date = models.DateTimeField('date published')
    slug = models.SlugField()
    content = models.TextField(blank=True)
    category = models.ForeignKey(Category)
    pic = models.ImageField(upload_to="news/", blank=True)

    is_draft = models.ImageField(blank=True, default=False)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(translify(self.name))
        super(NewsPost, self).save(*args, **kwargs)

    #def get_absolute_url(self):
    #    return reverse('company_details', args=[self.pk, self.slug])

    def __unicode__(self):
        return self.title        
        
