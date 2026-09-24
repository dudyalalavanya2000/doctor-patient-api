# Doctor Patient API

A REST API built using FastAPI for managing doctors and patients.

## Features

- Create and list doctors
- Get a doctor by ID
- Handle doctor not found errors
- Create and list patients
- Validate patient age
- Validate doctor email

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

## API Endpoints

### Doctors

- `POST /doctors` - Create a doctor
- `GET /doctors` - Get all doctors
- `GET /doctors/{doctor_id}` - Get a doctor by ID

### Patients

- `POST /patients` - Create a patient
- `GET /patients` - Get all patients

## Run the Project

Install the required packages:

```bash
pip install -r requirements.txt

