from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import models
from . import forms
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
class PatientList(ListView):
    model= models.Patient
class AddPatient(CreateView):
    model = models.Patient
    fields = "__all__"
    success_url = reverse_lazy('ListView')

class UpdatePatient(UpdateView):
    model= models.Patient
    fields = "__all__"
    success_url = reverse_lazy("ListView")
class DeletePatient(DeleteView):
    model= models.Patient
    success_url = reverse_lazy("ListView")

#CRUD operation for Doctors
class DoctorList(ListView):
    model= models.Doctor

class AddDoctor(CreateView):
    model= models.Doctor
    fields = '__all__'
    success_url = reverse_lazy('doctorList')
class UpdateDoctor(UpdateView):
    model = models.Doctor
    fields = '__all__'
    success_url = reverse_lazy('doctorList')

class DeleteDoctor(DeleteView):
    model= models.Doctor
    fields= '__all__'
    success_url = reverse_lazy('doctorList')
#Add doctor to patients
# def doctorPatientlink(request, )

#Add Patient clinical data to patient
def add_data(request, **kwargs):
    patient_data= models.Patient.objects.get(id = kwargs["pk"])
    patient_data_name= patient_data._meta.fields[1].name
    patient_object_val= getattr(patient_data,patient_data_name )
    form= forms.ClinicalForm()
    if request.method == 'POST':
        form = forms.ClinicalForm(request.POST)
        if form.is_valid():
            form.save()
        redirect("/")
    return render(request, "sdmcApp/add_patient_data.html", {"form": form , "patient_data": patient_data})

#Analyze the patient data
def analyze_data(request, **kwargs):
    patient_clinical_data= models.ClinicalData.objects.filter(patient_id= kwargs["pk"])
    response_data= []
    for eachEntry in patient_clinical_data:
        if eachEntry.componentName== "hw":
            heightWeight= eachEntry.componentValue.split("/")
            if len(heightWeight)> 1:
                feettoMeters= float(heightWeight[0]) * 0.4356
                BMI= float(heightWeight[1])/(feettoMeters * feettoMeters)
                bmiEntry= models.ClinicalData()
                bmiEntry.componentName= 'BMI'
                bmiEntry.componentValue= BMI
                response_data.append(bmiEntry)
        response_data.append(eachEntry)

    return render(request, 'sdmcApp/analyze_data.html', {'patient_clinical_data': response_data})

