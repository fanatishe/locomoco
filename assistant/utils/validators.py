def validate_phone(phone):
    if not phone.isdigit() or len(phone) != 10:
        raise ValueError("Phone must contain 10 digits.")
