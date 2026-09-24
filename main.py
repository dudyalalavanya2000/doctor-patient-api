from fastapi import FastAPI, HTTPException

from app.models import DoctorCreate, Doctor, PatientCreate, Patient
from app.database import doctors, patients
import app.database as database


app = FastAPI(
    title="Doctor Patient API",
    description="REST API for managing doctors and patients",
    version="1.0.0"
)


# =========================
# DOCTOR APIs
# =========================

@app.post("/doctors", response_model=Doctor, status_code=201)
def create_doctor(doctor: DoctorCreate):

    new_doctor = Doctor(
        id=database.doctor_id_counter,
        name=doctor.name,
        specialization=doctor.specialization,
        email=doctor.email,
        is_active=doctor.is_active
    )

    doctors.append(new_doctor)

    database.doctor_id_counter += 1

    return new_doctor


@app.get("/doctors", response_model=list[Doctor])
def get_doctors():

    return doctors


@app.get("/doctors/{doctor_id}", response_model=Doctor)
def get_doctor(doctor_id: int):

    for doctor in doctors:

        if doctor.id == doctor_id:
            return doctor

    raise HTTPException(
        status_code=404,
        detail="Doctor not found"
    )


# =========================
# PATIENT APIs
# =========================

@app.post("/patients", response_model=Patient, status_code=201)
def create_patient(patient: PatientCreate):

    new_patient = Patient(
        id=database.patient_id_counter,
        name=patient.name,
        age=patient.age,
        phone=patient.phone
    )

    patients.append(new_patient)

    database.patient_id_counter += 1

    return new_patient


@app.get("/patients", response_model=list[Patient])
def get_patients():

    return patients