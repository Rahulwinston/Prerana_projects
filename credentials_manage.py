# credentials_manage.py
import csv
from collections import namedtuple

Credential = namedtuple('Credential', ['username', 'password', 'role'])

class CredentialManager:
    def __init__(self, credential_file):
        self.credentials = self._load_credentials(credential_file)

    def _load_credentials(self, file_path):
        credentials = {}
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                username, password, role = row
                credentials[username] = Credential(username, password, role)
        return credentials

    def validate_user(self, username, password):
        if username in self.credentials:
            credential = self.credentials[username]
            if credential.password == password:
                return UserProfile(credential)
        return None

class UserProfile:
    def __init__(self, credential):
        self.username = credential.username
        self.role = credential.role

    def __str__(self):
        return f"Username: {self.username}, Role: {self.role}"