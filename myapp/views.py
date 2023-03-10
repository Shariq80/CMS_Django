from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from . models import Staff, PatientVisit, Patient, PatientBill, PatientFeedback, HealthHistory
from . forms import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'login.html')

def registerpage(request):
    form = createuserform()
    if request.method == 'POST':
        form = createuserform(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('index')


    context = {
        'form'  : form,
    }
    return render(request, 'register.html', context)

def home(request):
    return render(request, 'home.html')

def logoutuser(request):
    logout(request)
    return redirect('index')

def staffs(request):
    staffs = Staff.objects.all()
    return render(request, "myapp/staff.html", {"staffs": staffs})

def staff_details(request, id):
    staff = Staff.objects.get(pk=id)
    context = {
        "staff": staff
    }
    return render(request, "myapp/staff_details.html", context)

def add_staff(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = StaffForm()
        else:
            staff = Staff.objects.get(pk=id)
            form = StaffForm(instance=staff)
        return render(request, "myapp/add_staff.html", {"form": form})
    else:
        if id == 0:
            form = StaffForm(request.POST)
        else:
            staff = Staff.objects.get(pk=id)
            form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
        return redirect('staff')

def patients(request):
    patients = Patient.objects.all()
    context = {
        "patients": patients
    }
    return render(request, "myapp/patients.html", context)

def patient_details(request, id):
    patient = Patient.objects.get(pk=id)
    context = {
        "patient": patient
    }
    return render(request, "myapp/patient_details.html", context)

def add_patient(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PatientForm()
        else:
            patient = Patient.objects.get(pk=id)
            form = PatientForm(instance=patient)
        return render(request, "myapp/add_patient.html", {"form": form})
    else:
        if id == 0:
            form = PatientForm(request.POST)
        else:
            patient = Patient.objects.get(pk=id)
            form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
        return redirect('patients')

def visits(request):
    visits = PatientVisit.objects.all()
    visits_count = PatientVisit.objects.all().count()
    context = {
        "visits": visits,
        "visits_count": visits_count
    }
    return render(request, "myapp/visits.html", context)

def add_visit(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = VisitForm()
        else:
            visit = PatientVisit.objects.get(pk=id)
            form = PatientForm(instance=visit)
        return render(request, "myapp/add_visit.html", {"form": form})
    else:
        if id == 0:
            form = VisitForm(request.POST)
        else:
            visit = PatientVisit.objects.get(pk=id)
            form = VisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
        return redirect('visits')

def drugs(request):
    drugs = Drug.objects.all()
    return render(request, "myapp/drugs.html", {"drugs": drugs})

def drug_details(request, id):
    drug = Drug.objects.get(pk=id)
    context = {
        "drug": drug
    }
    return render(request, "myapp/drug_details.html", context)

def add_drug(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = DrugForm()
        else:
            drug = Drug.objects.get(pk=id)
            form = DrugForm(instance=drug)
        return render(request, "myapp/add_drug.html", {"form": form})
    else:
        if id == 0:
            form = DrugForm(request.POST)
        else:
            drug = Drug.objects.get(pk=id)
            form = DrugForm(request.POST, instance=drug)
        if form.is_valid():
            form.save()
        return redirect('drugs')

def suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, "myapp/suppliers.html", {"suppliers": suppliers})

def add_supplier(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = SupplierForm()
        else:
            supplier = Supplier.objects.get(pk=id)
            form = SupplierForm(instance=supplier)
        return render(request, "myapp/add_supplier.html", {"form": form})
    else:
        if id == 0:
            form = SupplierForm(request.POST)
        else:
            supplier = Supplier.objects.get(pk=id)
            form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
        return redirect('suppliers')

def supplier_details(request, id):
    supplier = Supplier.objects.get(pk=id)
    context = {
        "supplier": supplier
    }
    return render(request, "myapp/supplier_details.html", context)

def appointments(request):
    appointments = Appointment.objects.all()
    return render(request, "myapp/appointments.html", {"appointments": appointments})

def appointment_details(request, id):
    appointment = Appointment.objects.get(pk=id)
    context = {
        "appointment": appointment
    }
    return render(request, "myapp/appointment_details.html", context)

def add_appointment(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = AppointmentForm()
        else:
            appointment = Appointment.objects.get(pk=id)
            form = AppointmentForm(instance=appointment)
        return render(request, "myapp/add_appointment.html", {"form": form})
    else:
        if id == 0:
            form = AppointmentForm(request.POST)
        else:
            appointment = Appointment.objects.get(pk=id)
            form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
        return redirect('appointments')

def prescriptions(request):
    prescriptions = Prescription.objects.all()
    return render(request, "myapp/prescriptions.html", {"prescriptions": prescriptions})

def add_prescription(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PrescriptionForm()
        else:
            prescription = Prescription.objects.get(pk=id)
            form = PrescriptionForm(instance=prescription)
        return render(request, "myapp/add_prescription.html", {"form": form})
    else:
        if id == 0:
            form = PrescriptionForm(request.POST)
        else:
            prescription = Prescription.objects.get(pk=id)
            form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
        return redirect('prescriptions')

def prescription_details(request, id):
    prescription = Prescription.objects.get(pk=id)
    context = {
        "prescription": prescription
    }
    return render(request, "myapp/prescription_details.html", context)

def health_histories(request):
    health_histories = HealthHistory.objects.all()
    return render(request, "myapp/histories.html", {"health_histories": health_histories})

def add_health_history(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = HistoryForm()
        else:
            history = HealthHistory.objects.get(pk=id)
            form = HistoryForm(instance=history)
        return render(request, "myapp/add_history.html", {"form": form})
    else:
        if id == 0:
            form = HistoryForm(request.POST)
        else:
            history = HealthHistory.objects.get(pk=id)
            form = HistoryForm(request.POST, instance=history)
        if form.is_valid():
            form.save()
        return redirect('health_histories')

def bills(request):
    bills = PatientBill.objects.all()
    return render(request, "myapp/bills.html", {"bills": bills})

def add_bill(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = BillForm()
        else:
            bill = PatientBill.objects.get(pk=id)
            form = BillForm(instance=bill)
        return render(request, "myapp/add_bill.html", {"form": form})
    else:
        if id == 0:
            form = BillForm(request.POST)
        else:
            bill = PatientBill.objects.get(pk=id)
            form = BillForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
        return redirect('bills')

def feedback(request):
    feedbacks = PatientFeedback.objects.all()
    return render(request, "myapp/feedbacks.html", {"feedbacks": feedbacks})

def add_feedback(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = FeedbackForm()
        else:
            feedback = PatientFeedback.objects.get(pk=id)
            form = FeedbackForm(instance=feedback)
        return render(request, "myapp/add_feedback.html", {"form": form})
    else:
        if id == 0:
            form = FeedbackForm(request.POST)
        else:
            feedback = PatientFeedback.objects.get(pk=id)
            form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
        return redirect('feedbacks')

def feedback_details(request, id):
    feedback = PatientFeedback.objects.get(pk=id)
    context = {
        "feedback": feedback
    }
    return render(request, "myapp/feedback_details.html", context)
