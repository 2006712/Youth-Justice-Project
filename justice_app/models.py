from django.db import models


# -------------------------------
# BASE MODEL (for timestamps)
# -------------------------------
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# -------------------------------
# SUPPORT PROGRAM MODEL
# -------------------------------
class SupportProgram(BaseModel):
    PROGRAM_TYPES = [
        ('counselling', 'Counselling'),
        ('education', 'Education Support'),
        ('community', 'Community Service'),
        ('rehabilitation', 'Rehabilitation'),
    ]

    name = models.CharField(max_length=100)
    program_type = models.CharField(max_length=50, choices=PROGRAM_TYPES)
    description = models.TextField()
    eligibility_criteria = models.TextField()

    def __str__(self):
        return self.name


# -------------------------------
# YOUTH MODEL
# -------------------------------
class Youth(BaseModel):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    SCHOOL_STATUS_CHOICES = [
        ('Attending', 'Attending'),
        ('Dropped Out', 'Dropped Out'),
        ('Completed', 'Completed'),
    ]

    SUPPORT_LEVEL_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    school_status = models.CharField(max_length=20, choices=SCHOOL_STATUS_CHOICES)
    family_support_level = models.CharField(max_length=10, choices=SUPPORT_LEVEL_CHOICES)
    background_notes = models.TextField(blank=True)

    # Many-to-Many relationship
    support_programs = models.ManyToManyField(SupportProgram, blank=True)

    def __str__(self):
        return self.name

    # -------------------------------
    # BUSINESS LOGIC (HD level)
    # -------------------------------
    def recommend_programs(self):
        """
        Recommend programs based on offence severity and support level
        Demonstrates encapsulation (fat models, skinny views)
        """
        programs = SupportProgram.objects.all()

        # Get all offences for this youth
        offences = self.offence_set.all()

        # Default: return all programs if no offences
        if not offences.exists():
            return programs

        # Example logic
        for offence in offences:
            if offence.severity == 'Serious':
                return programs.filter(program_type='rehabilitation')

            elif offence.severity == 'Moderate':
                return programs.filter(program_type__in=['counselling', 'education'])

            elif offence.severity == 'Minor':
                return programs.filter(program_type='community')

        return programs


# -------------------------------
# OFFENCE MODEL
# -------------------------------
class Offence(BaseModel):
    OFFENCE_TYPES = [
        ('Theft', 'Theft'),
        ('Vandalism', 'Vandalism'),
        ('Assault', 'Assault'),
        ('Drug Related', 'Drug Related'),
        ('Other', 'Other'),
    ]

    SEVERITY_LEVELS = [
        ('Minor', 'Minor'),
        ('Moderate', 'Moderate'),
        ('Serious', 'Serious'),
    ]

    youth = models.ForeignKey(Youth, on_delete=models.CASCADE)
    offence_type = models.CharField(max_length=50, choices=OFFENCE_TYPES)
    severity = models.CharField(max_length=10, choices=SEVERITY_LEVELS)
    date_reported = models.DateField()

    def __str__(self):
        return f"{self.offence_type} - {self.youth.name}"