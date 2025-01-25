from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Competitor, Feature, FeatureValue

@admin.register(Competitor)
class CompetitorAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Competitors.
    """
    list_display = ('name', 'competitor_type', 'website', 'created_at', 'updated_at')
    list_filter = ('competitor_type', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'website')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (_('Basic Information'), {
            'fields': ('name', 'competitor_type', 'website'),
            'description': _("Basic details about the competitor."),
        }),
        (_('Description'), {
            'fields': ('description',),
            'description': _("Additional details or notes about the competitor."),
        }),
        (_('Timestamps'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
            'description': _("Automatically generated timestamps for record-keeping."),
        }),
    )
    list_per_page = 20


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Features.
    """
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    fieldsets = (
        (_('Feature Details'), {
            'fields': ('name', 'description'),
            'description': _("Define the feature and provide a description for clarity."),
        }),
    )
    list_per_page = 20


class FeatureValueInline(admin.TabularInline):
    """
    Inline editing for FeatureValues within the Competitor admin.
    """
    model = FeatureValue
    extra = 1  # Number of empty forms to display
    fields = ('feature', 'value')
    autocomplete_fields = ('feature',)  # Enable autocomplete for features


@admin.register(FeatureValue)
class FeatureValueAdmin(admin.ModelAdmin):
    """
    Admin interface for managing FeatureValues.
    """
    list_display = ('competitor', 'feature', 'value')
    list_editable = ('value',)
    list_select_related = ('competitor', 'feature')
    list_filter = ('competitor', 'feature__name')
    search_fields = ('competitor__name', 'feature__name', 'value')
    autocomplete_fields = ('competitor', 'feature')  # Enable autocomplete for competitors and features
    fieldsets = (
        (_('Feature Value Details'), {
            'fields': ('competitor', 'feature', 'value'),
            'description': _("Associate a competitor with a feature and provide its value."),
        }),
    )
    list_per_page = 20