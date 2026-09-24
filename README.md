# Doctor Patient API

A simple REST API built using Python, FastAPI, and Pydantic to manage doctors and patients.

## Technologies Used

* Python 3.9+
* FastAPI
* Pydantic
* Uvicorn
* In-memory storage

## Project Structure

```text
doctor-patient-api/
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   └── models.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd doctor-patient-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

Start the FastAPI server using:

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI provides interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

You can use Swagger UI to test all API endpoints.

## API Endpoints

### Doctor APIs

| Method | Endpoint               | Description      |
| ------ | ---------------------- | ---------------- |
| POST   | `/doctors`             | Create a doctor  |
| GET    | `/doctors`             | List all doctors |
| GET    | `/doctors/{doctor_id}` | Get doctor by ID |

### Patient APIs

| Method | Endpoint    | Description       |
| ------ | ----------- | ----------------- |
| POST   | `/patients` | Create a patient  |
| GET    | `/patients` | List all patients |

## Validation

The API includes the following validations:

* Doctor email must be a valid email address.
* Patient age must be greater than 0.
* Doctor `is_active` defaults to `true`.
* HTTP 404 is returned when a doctor is not found.
* Invalid input returns a validation error (HTTP 422).

## Example Doctor Request

```json
{
  "name": "Dr. Rathi",
  "specialization": "Cardiology",
  "email": "rathi@gmail.com",
  "is_active": true
}
```

## Example Patient Request

```json
{
  "name": "Meena",
  "age": 25,
  "phone": "9876543210"
}
```

