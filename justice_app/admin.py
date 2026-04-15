from django.contrib import admin
from .models import Youth, Offence, SupportProgram


@admin.register(Youth)
class YouthAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'school_status', 'family_support_level', 'created_at')
    search_fields = ('name', 'background_notes')
    list_filter = ('gender', 'school_status', 'family_support_level')


@admin.register(Offence)
class OffenceAdmin(admin.ModelAdmin):
    list_display = ('youth', 'offence_type', 'severity', 'date_reported')
    search_fields = ('offence_type', 'notes', 'youth__name')
    list_filter = ('severity', 'offence_type', 'date_reported')


@admin.register(SupportProgram)
class SupportProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'program_type', 'target_severity')
    search_fields = ('name', 'description')
    list_filter = ('program_type', 'target_severity')