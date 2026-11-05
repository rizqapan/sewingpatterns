# === Stage 2: Проверка полей ===
# Project: SewingPatterns
import re


def normalize_pattern_name(value):
    cleaned = value.strip().lower()
    cleaned = re.sub(r"[^a-zа-я0-9\s]", " ", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def normalize_pattern_type(value):
    mapping = {
        "юбка": "юбка",
        "платье": "платье",
        "блузка": "блузка",
        "рубашка": "рубашка",
        "кофта": "кофта",
        "куртка": "куртка",
        "пальто": "пальто",
        "шарф": "шарф",
        "сумка": "сумка",
        "обувь": "обувь",
    }
    normalized = normalize_pattern_name(value)
    return mapping.get(normalized, normalized)


def normalize_size(value):
    mapping = {
        "xs": "xs",
        "s": "s",
        "m": "m",
        "l": "l",
        "xl": "xl",
        "xxl": "xxl",
        "36": "36",
        "38": "38",
        "40": "40",
        "42": "42",
        "44": "44",
        "46": "46",
        "48": "48",
        "50": "50",
    }
    normalized = normalize_pattern_name(value).strip().upper()
    return mapping.get(normalized, normalized)


def normalize_difficulty(value):
    mapping = {
        "легко": "легко",
        "средне": "средне",
        "сложно": "сложно",
        "easy": "легко",
        "medium": "средне",
        "hard": "сложно",
        "1": "легко",
        "2": "средне",
        "3": "сложно",
    }
    normalized = normalize_pattern_name(value).strip().lower()
    return mapping.get(normalized, normalized)


class PatternValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"Поле «{field}»: {message}")


def validate_pattern_name(value):
    if value is None:
        raise PatternValidationError("название", "значение не может быть пустым")
    normalized = normalize_pattern_name(value)
    if not normalized:
        raise PatternValidationError("название", "неверный формат названия выкройки")
    return normalized


def validate_pattern_type(value):
    if value is None:
        raise PatternValidationError("тип", "значение не может быть пустым")
    normalized = normalize_pattern_type(value)
    if not normalized:
        raise PatternValidationError("тип", "неверный формат типа выкройки")
    return normalized


def validate_size(value):
    if value is None:
        raise PatternValidationError("размер", "значение не может быть пустым")
    normalized = normalize_size(value)
    if not normalized:
        raise PatternValidationError("размер", "неверный формат размера выкройки")
    return normalized


def validate_difficulty(value):
    if value is None:
        raise PatternValidationError("сложность", "значение не может быть пустым")
    normalized = normalize_difficulty(value)
    if not normalized:
        raise PatternValidationError("сложность", "неверный формат сложности выкройки")
    return normalized
