# patient_profile.py
from datetime import datetime

class PatientProfile:
    """
    Represents a patient's profile containing personal and demographic information.
    """
    def __init__(self, patient_id, gender, ethnicity, race, age, insurance_provider, zip_code):
        self.patient_id = patient_id
        self.gender = gender
        self.ethnicity = ethnicity
        self.race = race
        self.age = age
        self.insurance_provider = insurance_provider
        self.zip_code = zip_code
        self.visit_records = []

    def add_visit_record(self, visit_record):
        """
        Adds a new visit record to the patient's profile.
        
        Args:
            visit_record (VisitRecord): The visit record to be added.
        """
        self.visit_records.append(visit_record)