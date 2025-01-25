from django.db import models
from django.utils.translation import gettext_lazy as _

class Competitor(models.Model):
    """
    Represents a competitor in the market.
    Competitors can be direct, indirect, or potential.
    """
    COMPETITOR_TYPES = [
        ('direct', _('Direct Competitor')),
        ('indirect', _('Indirect Competitor')),
        ('potential', _('Potential Competitor')),
    ]

    name = models.CharField(
        max_length=255,
        unique=True,
        help_text=_("The name of the competitor."),
        db_comment="Stores the name of the competitor.",
    )
    competitor_type = models.CharField(
        max_length=10,
        choices=COMPETITOR_TYPES,
        help_text=_("The type of competitor (direct, indirect, or potential)."),
        db_comment="Stores the type of competitor.",
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text=_("A detailed description of the competitor."),
        db_comment="Stores a detailed description of the competitor.",
    )
    website = models.URLField(
        blank=True,
        null=True,
        help_text=_("The website URL of the competitor."),
        db_comment="Stores the website URL of the competitor.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("The date and time when the competitor was created."),
        db_comment="Stores the date and time when the competitor was created.",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text=_("The date and time when the competitor was last updated."),
        db_comment="Stores the date and time when the competitor was last updated.",
    )

    class Meta:
        verbose_name = _("Competitor")
        verbose_name_plural = _("Competitors")
        db_table_comment = "Stores information about competitors in the market."

    def __str__(self):
        return f"{self.name} ({self.competitor_type})"


class Feature(models.Model):
    """
    Represents a feature that can be used to compare competitors.
    Features can have values associated with multiple competitors.
    """
    name = models.CharField(
        max_length=255,
        help_text=_("The name of the feature (e.g., Pricing, Market Share)."),
        db_comment="Stores the name of the feature.",
    )
    competitors = models.ManyToManyField(
        Competitor,
        through='FeatureValue',
        help_text=_("The competitors associated with this feature."),
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text=_("A detailed description of the feature."),
        db_comment="Stores a detailed description of the feature.",
    )

    class Meta:
        verbose_name = _("Feature")
        verbose_name_plural = _("Features")
        db_table_comment = "Stores features used to compare competitors."

    def __str__(self):
        return self.name


class FeatureValue(models.Model):
    """
    Represents the value of a feature for a specific competitor.
    Links a feature, a competitor, and a value together.
    """
    feature = models.ForeignKey(
        Feature,
        on_delete=models.CASCADE,
        help_text=_("The feature associated with this value."),
        db_comment="Stores the feature associated with this value.",
    )
    competitor = models.ForeignKey(
        Competitor,
        on_delete=models.CASCADE,
        help_text=_("The competitor associated with this value."),
        db_comment="Stores the competitor associated with this value.",
    )
    value = models.CharField(
        max_length=255,
        help_text=_("The value of the feature for the competitor (e.g., 2.5, 40%)."),
        db_comment="Stores the value of the feature for the competitor.",
    )

    class Meta:
        unique_together = ('feature', 'competitor')  # Ensure each competitor has only one value per feature
        verbose_name = _("Feature Value")
        verbose_name_plural = _("Feature Values")
        db_table_comment = "Stores the values of features for specific competitors."

    def __str__(self):
        return f"{self.competitor.name} - {self.feature.name}: {self.value}"