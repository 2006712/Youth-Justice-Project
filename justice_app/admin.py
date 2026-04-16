from django.contrib import admin
from .models import Youth, Offence, SupportProgram


# =========================
# INLINE OFFENCE ADMIN
# =========================
class OffenceInline(admin.TabularInline):
    model = Offence
    extra = 1
    fields = ('offence_type', 'severity', 'date_reported', 'notes')
    show_change_link = True


# =========================
# YOUTH ADMIN
# =========================
@admin.register(Youth)
class YouthAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'gender',
        'school_status',
        'family_support_level',
        'created_at',
    )
    search_fields = (
        'name',
        'background_notes',
    )
    list_filter = (
        'gender',
        'school_status',
        'family_support_level',
    )
    ordering = ('-created_at',)
    filter_horizontal = ('support_programs',)
    inlines = [OffenceInline]


# =========================
# OFFENCE ADMIN
# =========================
@admin.register(Offence)
class OffenceAdmin(admin.ModelAdmin):
    list_display = (
        'youth',
        'offence_type',
        'severity',
        'date_reported',
    )
    search_fields = (
        'youth__name',
        'offence_type',
        'notes',
    )
    list_filter = (
        'severity',
        'date_reported',
    )
    ordering = ('-date_reported',)


# =========================
# SUPPORT PROGRAM ADMIN
# =========================
@admin.register(SupportProgram)
class SupportProgramAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'program_type',
    )
    search_fields = (
        'name',
        'description',
    )
    list_filter = (
        'program_type',
    )
    ordering = ('name',)