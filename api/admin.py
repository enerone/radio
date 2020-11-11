from django.contrib import admin
from .models import Station, Station_type, Group
# Register your models here.

class StationAdmin(admin.ModelAdmin):
    readonly_fields = ('main_image_preview',)
    list_display = ('name', 'frequency')
    ordering = ('name',)
    search_fields = ('name', 'frequency')
    
    def main_image_preview(self, obj):
        return obj.main_image_preview
    
    main_image_preview.short_description = 'Main Image preview'
    main_image_preview.allow_tags = True

admin.site.register(Station, StationAdmin)
admin.site.register(Station_type)
admin.site.register(Group)
