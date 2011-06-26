from django.contrib import admin
from control.models import SidebarLink, ContentBlock


class SidebarLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ('block_id', 'title', 'content')
    search_field = ('title', 'block_id')


admin.site.register(SidebarLink, SidebarLinkAdmin)
admin.site.register(ContentBlock, ContentBlockAdmin)
