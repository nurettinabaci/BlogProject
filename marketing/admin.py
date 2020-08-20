from django.contrib import admin
from .models import Subscriber, Newsletter


# Register your models here.

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp', 'confirmed')
    search_fields = ('email', 'timestamp')


class NewsletterAdmin(admin.ModelAdmin):
    actions = ['send_newsletter', ]

    def send_newsletter(self, request, queryset):
        for newsletter in queryset:
            newsletter.send(request)

    send_newsletter.short_description = "Send selected newsletters to all subscribers"


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
