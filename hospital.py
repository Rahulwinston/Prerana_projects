# hospital.py

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

# Visit Data Module
class VisitRecord:
    """
    Represents a record of a patient's visit to the hospital.
    """
    def __init__(self, visit_id, visit_date, department, chief_complaint):
        self.visit_id = visit_id
        self.visit_date = visit_date
        self.department = department
        self.chief_complaint = chief_complaint
        self.note_records = []

    def add_note_record(self, note_record):
        """
        Adds a new note record to the visit record.
        
        Args:
            note_record (NoteRecord): The note record to be added.
        """
        self.note_records.append(note_record)

class NoteRecord:
    """
    Represents a note or observation made during a patient's visit.
    """
    def __init__(self, note_id, note_type):
        self.note_id = note_id
        self.note_type = note_type

# Hospital Management System Module
class HospitalManagementSystem:
    """
    Manages patient records, visits, and notes for a hospital.
    """
    def __init__(self):
        self.patient_profiles = {}

    def add_patient_profile(self, patient_profile):
        """
        Adds a new patient profile to the hospital management system.
        
        Args:
            patient_profile (PatientProfile): The patient profile to be added.
        """
        self.patient_profiles[patient_profile.patient_id] = patient_profile

    def remove_patient_profile(self, patient_id):
        """
        Removes a patient profile from the hospital management system.
        
        Args:
            patient_id (str): The ID of the patient whose profile is to be removed.
        """
        if patient_id in self.patient_profiles:
            del self.patient_profiles[patient_id]

    def get_patient_profile(self, patient_id):
        """
        Retrieves a patient's profile from the hospital management system.
        
        Args:
            patient_id (str): The ID of the patient whose profile is to be retrieved.
        
        Returns:
            PatientProfile: The patient profile if found, None otherwise.
        """
        if patient_id in self.patient_profiles:
            return self.patient_profiles[patient_id]
        return None

    def count_visits_on_date(self, visit_date):
        """
        Counts the number of visits on a given date across all patient profiles.
        
        Args:
            visit_date (datetime.date): The date for which visits are to be counted.
        
        Returns:
            int: The total number of visits on the given date.
        """
        total_visits = 0
        for patient_profile in self.patient_profiles.values():
            for visit_record in patient_profile.visit_records:
                if visit_record.visit_date.date() == visit_date:
                    total_visits += 1
        return total_visits