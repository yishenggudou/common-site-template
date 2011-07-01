from django.contrib import admin
from control.models import SidebarLink, ContentBlock, Services


class SidebarLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ('block_id', 'title', 'content')
    search_field = ('title', 'block_id')

    class Media:
        js = [
            '/static/tiny_mce/tiny_mce.js',
            '/static/js/tinymce_setup.js',
        ]


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'slug', 'content')
    prepopulated_fields = {"slug": ("title",)}
    
    class Media:
        js = [
            '/static/tiny_mce/tiny_mce.js',
            '/static/js/tinymce_setup.js',
        ]        


admin.site.register(Services, ServicesAdmin)
admin.site.register(SidebarLink, SidebarLinkAdmin)
admin.site.register(ContentBlock, ContentBlockAdmin)
