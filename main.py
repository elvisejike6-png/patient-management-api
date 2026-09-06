from fastapi import FastAPI,HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from pydantic import BaseModel
import os

class Doctor(BaseModel):
    name : str
    speialization : str
    
class Patient(BaseModel):
    name : str
    age : int
    passport : str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

conn = sqlite3.connect("management.db")
cursor = conn.cursor()
conn.commit()
conn.close()

# add new doctor
@app.post("/add_doctor")
def add_doctor(doctor : Doctor) :
    conn = sqlite3.connect("management.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO doctors(name,specialization)VALUES(?,?)""",(doctor.name,doctor.speialization))
    conn.commit()
    conn.close()
    return {
        "message": "added successfully"
    }


# add new Patient
@app.post("/add_patient")
def add_patient(patient : Patient):
    conn = sqlite3.connect("management.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO patients(name,age,passport) VALUES(?,?,?)""",(patient.name,patient.age,patient.passport))
    conn.commit()
    conn.close
    return {
        "message":"added successfully"
    }
# view all Doctor
@app.get("/doctor")
def get_doctor():
    conn = sqlite3.connect("management.db")
    cursor =conn.cursor()
    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()
    conn.commit()
    conn.close()
    return doctors


# view Patient
@app.get("/patient")
def get_patient():
    conn = sqlite3.connect("management.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    conn.commit()
    conn.close()
    return patients
    
    # get individual Doctor
@app.get("/doctor/{id}")
def get_doctor(id: int):
    conn = sqlite3.connect("management.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors WHERE id=?",(id,))
    doctors =cursor.fetchone()
    conn.commit()
    conn.close()
    if doctors is None:
        raise HTTPException(status_code=404,detail="does not exist")
    return doctors

@app.get("/patient/{id}")
def get_patient(id: int):
    conn = sqlite3.connect("management.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE id=?",(id,))
    patients =cursor.fetchone()
    conn.commit()
    conn.close()
    if patients is None:
            raise HTTPException(status_code=404,detail="does not exist")
    return patients

@app.put("/doctor/{id}")
def update_doctor(id:int, doctor : Doctor):
    conn = sqlite3.connect("management.db")
    cursor =conn.cursor()
    cursor.execute("""UPDATE doctors SET name = ?, specialization = ? WHERE id =?""",(doctor.name,doctor.speialization,id))
    conn.commit()
    conn.close()
    return{
        "message":"Doctor updated successfully"
    }
    
    
@app.put("/patient/{id}")
def update_patient(id:int, patient : Patient):
    conn = sqlite3.connect("management.db")
    cursor =conn.cursor()
    cursor.execute("""UPDATE patients SET name = ?, age = ?, passport = ?  WHERE id =?""",(patient.name,patient.age,patient.passport,id))
    conn.commit()
    conn.close()
    return{
        "message":"patient updated successfully"
    }
    
@app.delete("/doctor/{id}")
def delete_doctor(id : int):
    conn = sqlite3.connect("management.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM doctors WHERE id =?",(id,))
    conn.commit()
    conn.close()
    return{
        "message": "Deleted Succesfully"
    }
    
@app.delete("/patient/{id}")
def delete_patient(id : int):
    conn = sqlite3.connect("management.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE id =?",(id,))
    conn.commit()
    conn.close()
    return{
        "message": "Deleted Succesfully"
    }
    
@app.get("/doctors/search")
def search_doctor(name : str):
    conn = sqlite3.connect("management.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM doctors WHERE name LIKE ?",(F"%{name}%",))
    doctors = cursor.fetchall()
    conn.close()
    return doctors

@app.get("/patients/search")
def search_doctor(name : str):
    conn = sqlite3.connect("management.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE name LIKE ?",(F"%{name}%",))
    Patients = cursor.fetchall()
    conn.close()
    return Patients

@app.post("/assigned")
def assigned_doctor(doctor_id : int, patient_id : int):
    conn=sqlite3.connect("management.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO assign(doctor_id,patient_id)VALUES(?,?)""",(doctor_id,patient_id))
    conn.commit()
    cursor.close()
    return{
        "message":"patient assigned succesfully"
    }
    
@app.put("/doctor/{doctor_id}/patient{patient.id}")
def update_assignment(doctor_id : int, patient_id : int):
    conn= sqlite3.connect("management.db")
    cursor = conn.cursor()
    cursor.execute("""UPDATE assign SET doctor_id =? WHERE patient_id=?""",(doctor_id,patient_id))
    conn.commit()
    conn.close()
    return{"message":"Updated succesfully"}

@app.post("/upload")
async def upload_file(file:UploadFile=File(...)):
    upload_folder = "upload"
    os.makedirs(upload_folder, exist_ok=True)  
    
    file_path = os.path.join(upload_folder,file.filename) 
    contents = await file.read()
    with open(file_path, "wb") as f:    
        f.write(contents)
        
    return{
        "message": "file uploaded succesfully",
        "file_name":file.filename
        
    }
    
