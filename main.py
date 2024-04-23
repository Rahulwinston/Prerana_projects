# main.py
import sys

from healthcare_system import HealthcareSystem

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <PA3_credentials.txt> <PA3_patients.csv>")
        sys.exit(1)

    healthcare_system = HealthcareSystem(sys.argv[1], sys.argv[2])
    healthcare_system.start_program()