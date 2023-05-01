from django.contrib import admin
from category.models import Categories

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Categories, CategoryAdmin)
