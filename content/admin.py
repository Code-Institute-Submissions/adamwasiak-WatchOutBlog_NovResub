from django.contrib import admin
from .models import Content


class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'content_type',
        'message',
    )

    ordering = ('email',)


admin.site.register(Content, ContentAdmin)
