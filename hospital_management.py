# hospital_management.py
class Hospital:
    def __init__(self):
        self.patient_records = {}

    def add_patient_record(self, patient_record):
        self.patient_records[patient_record.patient_id] = patient_record

    def remove_patient_record(self, patient_id):
        del self.patient_records[patient_id]

    def retrieve_patient_record(self, patient_id):
        if patient_id in self.patient_records:
            patient_record = self.patient_records[patient_id]
            print(f"Patient ID: {patient_record.patient_id}")
            print(f"Gender: {patient_record.gender}")
            print(f"Race: {patient_record.race}")
            print(f"Age: {patient_record.age}")
            print(f"Ethnicity: {patient_record.ethnicity}")
            print(f"Insurance: {patient_record.insurance}")
            print(f"Zip code: {patient_record.zip_code}")
            print("Visit records:")
            for visit_record in patient_record.visit_records:
                print(f"  Visit ID: {visit_record.visit_id}")
                print(f"  Visit time: {visit_record.visit_time}")
                print(f"  Department: {visit_record.department}")
                print(f"  Chief complaint: {visit_record.chief_complaint}")
                print("  Note records:")
                for note_record in visit_record.note_records:
                    print(f"    Note ID: {note_record.note_id}")
                    print(f"    Note type: {note_record.note_type}")
        else:
            print("Patient not found.")

    def count_visits_on_date(self, date):
        total_visits = 0
        for patient_record in self.patient_records.values():
            for visit_record in patient_record.visit_records:
                if visit_record.visit_time.date() == date.date():
                    total_visits += 1
        return total_visits

class PatientRecord:
    def __init__(self, patient_id, gender, race, age, ethnicity, insurance, zip_code):
        self.patient_id = patient_id
        self.gender = gender
        self.race = race
        self.age = age
        self.ethnicity = ethnicity
        self.insurance = insurance
        self.zip_code = zip_code
        self.visit_records = []

    def add_visit_record(self, visit_record):
        self.visit_records.append(visit_record)

class VisitRecord:
    def __init__(self, visit_id, visit_time, department, chief_complaint):
        self.visit_id = visit_id
        self.visit_time = visit_time
        self.department = department
        self.chief_complaint = chief_complaint
        self.note_records = []

    def add_note_record(self, note_record):
        self.note_records.append(note_record)