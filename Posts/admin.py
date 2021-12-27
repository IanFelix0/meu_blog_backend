from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'date_added', 'date_change')
    search_fields = ('title',)


admin.site.register(Post,PostAdmin)
