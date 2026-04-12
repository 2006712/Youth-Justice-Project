from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Base model (for timestamps)
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Youth model
class Youth(BaseModel):
    SCHOOL_STATUS_CHOICES = [
        ('attending', 'Attending'),
        ('dropped', 'Dropped Out'),
        ('completed', 'Completed'),
    ]

    FAMILY_SUPPORT_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[MinValueValidator(10), MaxValueValidator(25)])
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    background_notes = models.TextField(blank=True)
    school_status = models.CharField(max_length=20, choices=SCHOOL_STATUS_CHOICES)
    family_support_level = models.CharField(max_length=10, choices=FAMILY_SUPPORT_CHOICES)

    def get_recent_offences(self):
        return self.offences.order_by('-date_reported')[:3]

    def __str__(self):
        return self.name


# Offence model
class Offence(BaseModel):
    SEVERITY_CHOICES = [
        ('minor', 'Minor'),
        ('moderate', 'Moderate'),
        ('serious', 'Serious'),
    ]

    OFFENCE_TYPE_CHOICES = [
        ('theft', 'Theft'),
        ('vandalism', 'Vandalism'),
        ('assault', 'Assault'),
        ('drug_related', 'Drug Related'),
        ('other', 'Other'),
    ]

    youth = models.ForeignKey(
        Youth,
        on_delete=models.CASCADE,
        related_name='offences'
    )

    offence_type = models.CharField(max_length=30, choices=OFFENCE_TYPE_CHOICES)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    date_reported = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.offence_type} - {self.youth.name}"