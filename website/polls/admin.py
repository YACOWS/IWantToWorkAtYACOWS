from django.contrib import admin

from polls.models import Poll, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    readonly_fields = ('votes',)

class PollAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline
    ]
    list_display = ('question', 'pub_date')

admin.site.register(Poll, PollAdmin)