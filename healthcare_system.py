# healthcare_system.py
from datetime import datetime
import csv

from credentials_manage import CredentialManager
from hospital_management import Hospital, PatientRecord, VisitRecord
from patient_profile import PatientProfile
from visit_record import VisitRecord, NoteRecord

class HealthcareSystem:
    def __init__(self, credentials_file, patient_data_file):
        self.credentials_manager = CredentialManager(credentials_file)
        self.hospital = Hospital()
        self.load_patient_data(patient_data_file)

   
    def load_patient_data(self, file_path):
        """
        Load patient data from a CSV file into the hospital object.

        Args:
            file_path (str): Path to the CSV file containing patient data.
        """
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                patient_id = row['Patient_ID']
                gender = row['Gender']
                race = row['Race']
                age = int(row['Age'])
                ethnicity = row['Ethnicity']
                insurance = row['Insurance']
                zip_code = row['Zip_code']
                visit_id = row['Visit_ID']
                visit_time = datetime.strptime(row['Visit_time'], '%Y-%m-%d')
                department = row['Visit_department']
                chief_complaint = row['Chief_complaint']
                visit_record = VisitRecord(visit_id, visit_time, department, chief_complaint)

                # Check if patient already exists, if not, create a new patient record
                if patient_id not in self.hospital.patient_records:
                    patient_record = PatientRecord(patient_id, gender, race, age, ethnicity, insurance, zip_code)
                    self.hospital.add_patient_record(patient_record)
                else:
                    patient_record = self.hospital.patient_records[patient_id]

                # Associate visit record with patient record
                patient_record.add_visit_record(visit_record)
                note_id = row['Note_ID']
                note_type = row['Note_type']
                note_record = NoteRecord(note_id, note_type)
                visit_record.add_note_record(note_record)

    def start_program(self):
        """
        Start the healthcare program by logging in and performing actions based on user role.
        """
        user = self.authenticate_user()
        if user.role == 'admin':
            self.admin_actions()
        elif user.role == 'management':
            self.management_actions()
        elif user.role in ['clinician', 'nurse']:
            self.clinician_nurse_actions()

    def admin_actions(self):
        """
        Perform actions for admin users.
        """
        print("You are logged in as an admin.")
        print("You can only perform 'count_visits' action.")
        action = input("Enter 'count_visits' or 'stop': ").strip().lower()
        if action == 'count_visits':
            date_str = input("Enter date (YYYY-MM-DD): ")
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d')
                total_visits = self.hospital.count_visits_on_date(date)
                print("Total visits on", date.strftime('%Y-%m-%d'), ":", total_visits)
            except ValueError:
                print("Invalid date format.")
        elif action == 'stop':
            print("Exiting program.")
            exit()
        else:
            print("Invalid action. Exiting program.")
            exit()

    def management_actions(self):
        """
        Perform actions for management users.
        """
        print("You are logged in as management.")

        self.generate_key_statistics()
        print("Statistics generated. Exiting program.")
        exit()

    def clinician_nurse_actions(self):
        """
        Perform actions for clinician and nurse users.
        """
        print("You are logged in as a clinician/nurse.")
        print("You can perform all actions.")
        while True:
            action = input("Enter 'add_patient', 'remove_patient', 'retrieve_patient', 'count_visits', or 'stop': ").strip().lower()
            if action == 'add_patient':
                self.add_patient_record()
            elif action == 'remove_patient':
                self.remove_patient_record()
            elif action == 'retrieve_patient':
                patient_id = input("Enter Patient_ID: ")
                self.hospital.retrieve_patient_record(patient_id)
            elif action == 'count_visits':
                date_str = input("Enter date (YYYY-MM-DD): ")
                try:
                    date = datetime.strptime(date_str, '%Y-%m-%d')
                    total_visits = self.hospital.count_visits_on_date(date)
                    print("Total visits on", date.strftime('%Y-%m-%d'), ":", total_visits)
                except ValueError:
                    print("Invalid date format.")
            elif action == 'stop':
                print("Exiting program.")
                exit()
            else:
                print("Invalid action. Please try again.")

    def add_patient_record(self):
        """
        Add a new patient record to the hospital.
        """
        patient_id = input("Enter Patient_ID: ")
        if patient_id in self.hospital.patient_records:
            print("Patient already exists.")
            return
        gender = input("Enter Gender: ")
        race = input("Enter Race: ")
        age = int(input("Enter Age: "))
        ethnicity = input("Enter Ethnicity: ")
        insurance = input("Enter Insurance: ")
        zip_code = input("Enter Zip code: ")
        patient_record = PatientRecord(patient_id, gender, race, age, ethnicity, insurance, zip_code)
        self.hospital.add_patient_record(patient_record)
        print("Patient added successfully.")

    def remove_patient_record(self):
        """
        Remove a patient record from the hospital.
        """
        patient_id = input("Enter Patient_ID: ")
        if patient_id in self.hospital.patient_records:
            self.hospital.remove_patient_record(patient_id)
            print("Patient removed successfully.")
        else:
            print("Patient not found.")

    def generate_key_statistics(self):
        """
        Generate key statistics reports based on patient data.
        """
        print("Generating key statistics reports...")
        # Initialize dictionaries to store statistics
        patients_count = {}
        insurance_count = {}
        demographics_count = {'age': {}, 'race': {}, 'gender': {}, 'ethnicity': {}}

        # Collect statistics from patient data
        for patient_record in self.hospital.patient_records.values():
            # Count total patients
            patients_count[patient_record.patient_id] = patients_count.get(patient_record.patient_id, 0) + 1

            # Count insurance types
            insurance_count[patient_record.insurance] = insurance_count.get(patient_record.insurance, 0) + 1

            # Count demographics
            demographics_count['age'][patient_record.age] = demographics_count['age'].get(patient_record.age, 0) + 1
            demographics_count['race'][patient_record.race] = demographics_count['race'].get(patient_record.race, 0) + 1
            demographics_count['gender'][patient_record.gender] = demographics_count['gender'].get(patient_record.gender, 0) + 1
            demographics_count['ethnicity'][patient_record.ethnicity] = demographics_count['ethnicity'].get(patient_record.ethnicity, 0) + 1

        # Print key statistics
        print("\n1. Temporal trend of the number of patients who visited the hospital with different types of insurances:")
        for insurance, count in insurance_count.items():
            print(f"   - Insurance: {insurance}, Number of patients: {count}")

        print("\n2. Temporal trend of the number of patients who visited the hospital in different demographics groups:")
        for category, data in demographics_count.items():
            print(f"   - Demographic category: {category}")
            for group, count in data.items():
                print(f"     - {group}: {count}")

        print("Key statistics reports generated successfully.")