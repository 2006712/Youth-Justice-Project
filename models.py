from django.db import models
from django.utils import timezone


class Youth(models.Model):
    RISK_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    background_notes = models.TextField(blank=True)
    school_status = models.CharField(max_length=100)
    family_support_level = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def calculate_risk_level(self):
        offences = self.offence_set.all()
        total_offences = offences.count()

        if total_offences == 0:
            return "LOW"

        serious_count = offences.filter(severity='SERIOUS').count()
        moderate_count = offences.filter(severity='MODERATE').count()
        minor_count = offences.filter(severity='MINOR').count()

        if serious_count >= 1:
            return "HIGH"

        if moderate_count >= 2:
            return "HIGH"

        if minor_count >= 2:
            return "MEDIUM"

        if moderate_count == 1:
            return "MEDIUM"

        return "LOW"

    def get_recent_offences(self):
        return self.offence_set.order_by('-date_reported')[:3]


class Offence(models.Model):
    SEVERITY_CHOICES = [
        ('MINOR', 'Minor'),
        ('MODERATE', 'Moderate'),
        ('SERIOUS', 'Serious'),
    ]

    youth = models.ForeignKey(
        Youth,
        on_delete=models.CASCADE,
        related_name='offence_set'
    )

    offence_type = models.CharField(max_length=100)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    date_reported = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.offence_type} - {self.severity}"
