from django.contrib import admin

from .models import Newsletter, Subscriber


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'owner',)
    search_fields = ('name', 'content', 'owner')
    empty_value_display = 'NULL'


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'surname', 'email', 'birth_date')
    search_fields = ('name', 'surname', 'email')
    list_filter = ('birth_date',)
    empty_value_display = 'NULL'


admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
