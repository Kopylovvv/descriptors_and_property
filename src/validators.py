def validate_string(value):
    """Валидатор для строковых значений"""
    if not isinstance(value, str):
        raise TypeError(f"Ожидается строка, получен {type(value).__name__}")
    if not value or not value.strip():
        raise ValueError("Значение не может быть пустым")
    return value.strip()


def validate_priority(value):
    """Валидатор для приоритета"""
    valid_priorities = ["низкий", "обычный", "высокий"]
    if value not in valid_priorities:
        raise ValueError(
            f"Приоритет должен быть одним из: {', '.join(valid_priorities)}. "
            f"Получен: '{value}'"
        )
    return value


def validate_status(value):
    """Валидатор для статуса"""
    valid_statuses = ["не начата", "в работе", "завершена", "отменена", "провалена"]
    if value not in valid_statuses:
        raise ValueError(
            f"Статус должен быть одним из: {', '.join(valid_statuses)}. "
            f"Получен: '{value}'"
        )
    return value
