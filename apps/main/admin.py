from django.contrib import admin
from main.models import Services


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'slug', 'content')
    prepopulated_fields = {"slug": ("title",)}
    
    class Media:
        js = [
            '/static/tiny_mce/tiny_mce.js',
            '/static/js/tinymce_setup.js',
        ]        


admin.site.register(Services, ServicesAdmin)
