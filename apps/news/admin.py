from django.contrib import admin
from news.models import Category, NewsPost


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    prepopulated_fields = {"slug": ("title",)}


class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'text', 'pub_date')
    search_field = ('title', 'pub_date')
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        js = [
            '/static/tiny_mce/tiny_mce.js',
            '/static/js/tinymce_setup.js',
        ]

admin.site.register(Category, CategoryAdmin)
admin.site.register(NewsPost, NewsPostAdmin)
