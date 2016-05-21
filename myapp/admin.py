# -*- coding: utf-8 -*-
from django.contrib.admin import ModelAdmin

from myapp.models import Article
from django.contrib import admin


class ArticleAdmin(ModelAdmin):
    list_display = ("title", "created_at")
    # prepopulated_fields = {
    #     "slug": ("title",),
    #     "summary": ("content",),
    #    }  # 填title的时候自动填充slug
    # readonly_fields = ('slug', 'summary')

admin.site.register(Article, ArticleAdmin)