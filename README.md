# Patient Management System API

A backend application for managing doctors, patients and doctor-patient assignments.

## Features

- Add, view, update and delete doctors
- Add, view, update and delete patients
- Search for doctors and patients
- Assign doctors to patients
- Update doctor-patient assignments
- Upload files

## Technologies

- Python
- FastAPI
- SQLite
- Pydantic

## How to Run the Project

Install the required packages:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
uvicorn main:app --reload
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```