from django.contrib import admin
from .models import LearningJourney, AboutMe, AdminScreenshot

@admin.register(LearningJourney)
class LearningJourneyAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'date_learned']
    list_filter = ['category', 'date_learned']
    search_fields = ['title', 'description']

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['name', 'student_id', 'bio_preview']
    fieldsets = [
        ('Personal Information', {
            'fields': ['name', 'student_id', 'profile_picture']
        }),
        ('About Me', {
            'fields': ['bio', 'interests']
        }),
    ]
    
    def bio_preview(self, obj):
        return obj.bio[:50] + '...' if len(obj.bio) > 50 else obj.bio
    bio_preview.short_description = 'Bio Preview'

@admin.register(AdminScreenshot)
class AdminScreenshotAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_order']
    list_editable = ['display_order']