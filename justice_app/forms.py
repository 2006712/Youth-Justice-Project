from django import forms
from .models import Youth, Offence, SupportProgram


class YouthForm(forms.ModelForm):
    class Meta:
        model = Youth
        fields = ['name', 'age', 'gender', 'school_status', 'family_support_level', 'background_notes']


class OffenceForm(forms.ModelForm):
    class Meta:
        model = Offence
        fields = ['youth', 'offence_type', 'severity', 'date_reported', 'notes']


class SupportProgramForm(forms.ModelForm):
    class Meta:
        model = SupportProgram
        fields = ['name', 'program_type', 'target_severity', 'description']