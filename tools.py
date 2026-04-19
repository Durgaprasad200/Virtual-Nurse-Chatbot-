def get_medications(nurse):
    return nurse.get_medications()

def get_appointments(nurse):
    return nurse.get_appointments()

def get_vitals(nurse):
    return nurse.get_vital_signs()

def add_medication(nurse, data):
    return nurse.add_medication(
        data.get("name"),
        data.get("dosage"),
        data.get("schedule")
    )

def add_vital(nurse, data):
    return nurse.add_vital_sign(
        data.get("type"),
        data.get("value")
    )
