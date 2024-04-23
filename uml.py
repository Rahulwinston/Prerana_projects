from plantuml import PlantUML

@PlantUML.apply
def draw_uml():
    yield r"""
@startuml
class HealthcareSystem {
    - credentials_manager: CredentialManager
    - hospital: Hospital
    __
    + __init__(credentials_file, patient_data_file)
    + load_patient_data(file_path)
    + start_program()
    + admin_actions()
    + management_actions()
    + clinician_nurse_actions()
    + add_patient_record()
    + remove_patient_record()
    + generate_key_statistics()
    + authenticate_user()
}

class CredentialManager {
    - credentials: dict
    __
    + __init__(credential_file)
    - _load_credentials(file_path)
    + validate_user(username, password)
}

class UserProfile {
    - username: str
    - role: str
    __
    + __init__(credential)
    + __str__()
}

class Hospital {
    - patient_records: dict
    __
    + __init__()
    + add_patient_record(patient_record)
    + remove_patient_record(patient_id)
    + retrieve_patient_record(patient_id)
    + count_visits_on_date(date)
}

class PatientRecord {
    - patient_id: str
    - gender: str
    - race: str
    - age: int
    - ethnicity: str
    - insurance: str
    - zip_code: str
    - visit_records: list
    __
    + __init__(patient_id, gender, race, age, ethnicity, insurance, zip_code)
    + add_visit_record(visit_record)
}

class VisitRecord {
    - visit_id: str
    - visit_time: datetime
    - department: str
    - chief_complaint: str
    - note_records: list
    __
    + __init__(visit_id, visit_time, department, chief_complaint)
    + add_note_record(note_record)
}

class NoteRecord {
    - note_id: str
    - note_type: str
    __
    + __init__(note_id, note_type)
}

HealthcareSystem --> CredentialManager
HealthcareSystem --> Hospital
CredentialManager --> UserProfile
Hospital --> PatientRecord
PatientRecord --> VisitRecord
VisitRecord --> NoteRecord
@enduml
"""

if __name__ == "__main__":
    draw_uml()