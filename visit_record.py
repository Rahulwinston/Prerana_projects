# visit_record.py
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