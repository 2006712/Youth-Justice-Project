from django import forms
from .models import Youth, Offence, SupportProgram


# -------------------------------
# YOUTH FORM
# -------------------------------
class YouthForm(forms.ModelForm):
    class Meta:
        model = Youth
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'school_status': forms.Select(attrs={'class': 'form-control'}),
            'family_support_level': forms.Select(attrs={'class': 'form-control'}),
            'background_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


# -------------------------------
# OFFENCE FORM
# -------------------------------
class OffenceForm(forms.ModelForm):
    class Meta:
        model = Offence
        fields = '__all__'
        widgets = {
            'youth': forms.Select(attrs={'class': 'form-control'}),
            'offence_type': forms.Select(attrs={'class': 'form-control'}),
            'severity': forms.Select(attrs={'class': 'form-control'}),
            'date_reported': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }


# -------------------------------
# SUPPORT PROGRAM FORM
# -------------------------------
class SupportProgramForm(forms.ModelForm):
    class Meta:
        model = SupportProgram
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'program_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'eligibility_criteria': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }