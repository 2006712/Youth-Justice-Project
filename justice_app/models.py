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
        
    def recommend_programs(self):
<<<<<<< HEAD
        return SupportProgram.objects.eligible_for_youth(self)
=======
        return SupportProgram.objects.eligible_for_youth(self)    
>>>>>>> f3b933501d711867153131853a38a2e4b92c2fbd


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
    
    
class SupportProgramManager(models.Manager):
    def eligible_for_youth(self, youth):
        return self.filter(
            supported_risk_level=youth.calculate_risk_level(),
            minimum_age__lte=youth.age,
            maximum_age__gte=youth.age,
            active=True
        )

class SupportProgram(models.Model):
    CATEGORY_CHOICES = [
        ('counselling', 'Counselling'),
        ('training', 'Training'),
        ('community_service', 'Community Service'),
    ]

    RISK_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    description = models.TextField()
    minimum_age = models.PositiveIntegerField()
    maximum_age = models.PositiveIntegerField()
    supported_risk_level = models.CharField(max_length=10, choices=RISK_CHOICES)
    active = models.BooleanField(default=True)

    objects = SupportProgramManager()

    def __str__(self):
        return self.name
    

class Recommendation(BaseModel):
    STATUS_CHOICES = [
        ('suggested', 'Suggested'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
    ]

    youth = models.ForeignKey(Youth, on_delete=models.CASCADE)
    support_program = models.ForeignKey(SupportProgram, on_delete=models.CASCADE)
    recommendation_reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='suggested')

    def __str__(self):
        return f"{self.youth} -> {self.support_program}"
