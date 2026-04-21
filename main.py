from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,EmailStr,Field
from typing import List
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hospital API Running Successfully"}
doctors = []
patients = []
doctor_id_counter = 1
patient_id_counter = 1
class DoctorCreate(BaseModel):
    name: str
    specialization: str
    email: EmailStr 
    is_active: bool = True
class DoctorCreate(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    is_active: bool = True
class DoctorResponse(DoctorCreate):
    id: int
class PatientCreate(BaseModel):
    name: str
    age: int = Field(..., gt=0)
    phone: str
class PatientResponse(PatientCreate):
    id: int
@app.post("/doctors", response_model=DoctorResponse)
def create_doctor(doctor: DoctorCreate):
    global doctor_id_counter

    new_doctor = {
        "id": doctor_id_counter,
        "name": doctor.name,
        "specialization": doctor.specialization,
        "email": doctor.email,
        "is_active": doctor.is_active
    }

    doctors.append(new_doctor)
    doctor_id_counter += 1
    return new_doctor
@app.get("/doctors", response_model=List[DoctorResponse])
def get_doctors():
    return doctors
@app.get("/doctors/{doctor_id}", response_model=DoctorResponse)
def get_doctor(doctor_id: int):
    for doctor in doctors:
        if doctor["id"] == doctor_id:
            return doctor

    raise HTTPException(status_code=404, detail="Doctor not found")


@app.post("/patients", response_model=PatientResponse)
def create_patient(patient: PatientCreate):
    global patient_id_counter

    new_patient = {
        "id": patient_id_counter,
        "name": patient.name,
        "age": patient.age,
        "phone": patient.phone
    }
    patients.append(new_patient)
    patient_id_counter += 1
    return new_patient


@app.get("/patients", response_model=List[PatientResponse])
def get_patients():
    return patients