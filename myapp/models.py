from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, allow_unicode=True)
            self.summary = self.content[:200]
        return super(Article, self).save(*args, **kwargs)