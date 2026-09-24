from pydantic import BaseModel, EmailStr, Field


class DoctorCreate(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    is_active: bool = True


class Doctor(DoctorCreate):
    id: int


class PatientCreate(BaseModel):
    name: str
    age: int = Field(gt=0)
    phone: str


class Patient(PatientCreate):
    id: int