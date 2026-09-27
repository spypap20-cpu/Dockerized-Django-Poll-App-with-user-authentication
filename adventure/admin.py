from django.contrib import admin

from .models import Choice, Story

class ChoiceInline(admin.TabularInline):
     model = Choice
     fk_name = 'current_scene'
     

class StoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title", {"fields": ["title"]}),
        ("Story text", {"fields": ["story_text", "is_start"]})
    ]
    inlines = [ChoiceInline]
    list_display = ["title", "story_text", "is_start"]
    list_filter = ["is_start"] 
    search_fields = ["title"]

admin.site.register(Story, StoryAdmin)

