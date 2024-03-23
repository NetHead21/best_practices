def get_user_input(label: str, required: bool = True) -> str:
    value = input(f"{label}: ") or None
    while required and not value:
        value = input(f"{label}: ") or None
    return value
