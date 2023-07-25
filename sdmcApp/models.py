from django.db import models

# Create your models here.
class Doctor(models.Model):
    firstName= models.CharField(max_length = 20)
    lastName = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)
    mobile= models.CharField(max_length = 13)



class Patient(models.Model):
    firstName= models.CharField(max_length = 20)
    lastName= models.CharField(max_length = 20)
    age= models.IntegerField()
    doctor= models.ForeignKey(Doctor, on_delete = models.CASCADE, null = True)

class ClinicalData(models.Model):
    COMPONENT_NAMES= [('hw', 'height/ weight'), ('bp', 'Blood Pressure'), ('hrt', 'Heart rate')]
    componentName= models.CharField(choices = COMPONENT_NAMES, max_length = 20)
    componentValue= models.CharField(max_length = 20)
    measuredDateTime= models.DateTimeField(auto_now_add = True)
    patient= models.ForeignKey(Patient,on_delete = models.CASCADE)



