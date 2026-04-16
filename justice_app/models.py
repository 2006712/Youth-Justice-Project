from django.db import models


# =========================
# SUPPORT PROGRAM MODEL
# =========================
class SupportProgram(models.Model):
    PROGRAM_TYPES = [
        ("Community", "Community"),
        ("Counselling", "Counselling"),
        ("Education", "Education"),
        ("Rehabilitation", "Rehabilitation"),
        ("Intensive Support", "Intensive Support"),
        ("Mentoring", "Mentoring"),
    ]

    name = models.CharField(max_length=100)
    program_type = models.CharField(max_length=50, choices=PROGRAM_TYPES)
    description = models.TextField()

    def __str__(self):
        return self.name


# =========================
# YOUTH MODEL
# =========================
class Youth(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    SCHOOL_STATUS_CHOICES = [
        ("Attending", "Attending"),
        ("Dropped Out", "Dropped Out"),
    ]

    SUPPORT_LEVEL_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    school_status = models.CharField(max_length=20, choices=SCHOOL_STATUS_CHOICES)
    family_support_level = models.CharField(max_length=10, choices=SUPPORT_LEVEL_CHOICES)
    background_notes = models.TextField(blank=True)

    # Relationship to programs
    support_programs = models.ManyToManyField(SupportProgram, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    # =========================
    # RECOMMENDATION LOGIC (HD LEVEL)
    # =========================
    def recommend_programs(self):
        """
        Rule-based recommendation system using offence severity + personal context
        """

        programs = SupportProgram.objects.none()

        # Get latest offence
        latest_offence = self.offences.order_by('-date_reported').first()

        if not latest_offence:
            return programs

        severity = latest_offence.severity

        # 🔥 Core decision logic
        if severity == "Minor":
            programs = SupportProgram.objects.filter(program_type="Community")

        elif severity == "Moderate":
            programs = SupportProgram.objects.filter(
                program_type__in=["Counselling", "Education"]
            )

        elif severity == "Serious":
            programs = SupportProgram.objects.filter(
                program_type__in=["Rehabilitation", "Intensive Support"]
            )

        # 🔥 Context-aware improvements
        if self.family_support_level == "Low":
            programs = programs | SupportProgram.objects.filter(program_type="Mentoring")

        if self.school_status == "Dropped Out":
            programs = programs | SupportProgram.objects.filter(program_type="Education")

        return programs.distinct()


# =========================
# OFFENCE MODEL
# =========================
class Offence(models.Model):
    SEVERITY_CHOICES = [
        ("Minor", "Minor"),
        ("Moderate", "Moderate"),
        ("Serious", "Serious"),
    ]

    youth = models.ForeignKey(
        Youth,
        on_delete=models.CASCADE,
        related_name="offences"
    )

    offence_type = models.CharField(max_length=100)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    notes = models.TextField(blank=True)
    date_reported = models.DateField()

    def __str__(self):
        return f"{self.youth.name} - {self.offence_type}"