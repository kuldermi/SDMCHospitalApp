from django import forms
from . import models
class PatientForm(forms.ModelForm):
    class Meta:
        model = models.Patient
        fields= "__all__"

class ClinicalForm(forms.ModelForm):
    class Meta:
        model= models.ClinicalData
        fields= "__all__"

