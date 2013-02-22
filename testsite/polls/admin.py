from django.contrib import admin
from polls.models import Poll, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date')
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 
            'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
