from django.contrib import admin
from tag.models import Tags

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Tags, TagAdmin)
