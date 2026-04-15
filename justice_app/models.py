from django.db import models


# Base model for timestamps
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Youth model
class Youth(BaseModel):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    SCHOOL_STATUS_CHOICES = [
        ('attending', 'Attending'),
        ('dropped', 'Dropped Out'),
        ('completed', 'Completed'),
    ]

    SUPPORT_LEVEL_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    school_status = models.CharField(max_length=20, choices=SCHOOL_STATUS_CHOICES)
    family_support_level = models.CharField(max_length=10, choices=SUPPORT_LEVEL_CHOICES)
    background_notes = models.TextField(blank=True)

    # NEW: Support programs relationship
    support_programs = models.ManyToManyField('SupportProgram', blank=True)

    def get_recent_offences(self):
        return self.offences.all().order_by('-date_reported')[:5]

    def __str__(self):
        return self.name


# Offence model
class Offence(BaseModel):
    SEVERITY_CHOICES = [
        ('minor', 'Minor'),
        ('moderate', 'Moderate'),
        ('serious', 'Serious'),
    ]

    OFFENCE_TYPES = [
        ('theft', 'Theft'),
        ('vandalism', 'Vandalism'),
        ('assault', 'Assault'),
        ('drug', 'Drug Related'),
        ('other', 'Other'),
    ]

    youth = models.ForeignKey(
        Youth,
        on_delete=models.CASCADE,
        related_name='offences'
    )

    offence_type = models.CharField(max_length=50, choices=OFFENCE_TYPES)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    date_reported = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.offence_type} - {self.youth.name}"


# Support Program model (NEW)
class SupportProgram(models.Model):
    PROGRAM_TYPES = [
        ('counselling', 'Counselling'),
        ('training', 'Skill Training'),
        ('community', 'Community Service'),
    ]

    SEVERITY_LEVELS = [
        ('minor', 'Minor'),
        ('moderate', 'Moderate'),
        ('serious', 'Serious'),
    ]

    name = models.CharField(max_length=100)
    program_type = models.CharField(max_length=20, choices=PROGRAM_TYPES)
    target_severity = models.CharField(max_length=20, choices=SEVERITY_LEVELS)
    description = models.TextField()

    def __str__(self):
        return self.name