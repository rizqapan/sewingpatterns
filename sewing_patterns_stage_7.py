# === Stage 7: Связи между сущностями ===
# Project: SewingPatterns
from collections import defaultdict


class Pattern:
    def __init__(self, name, pattern_type, size, difficulty):
        self.name = name
        self.pattern_type = pattern_type
        self.size = size
        self.difficulty = difficulty


class Detail:
    def __init__(self, id, name, pattern_id):
        self.id = id
        self.name = name
        self.pattern_id = pattern_id


class IntegrityError(Exception):
    pass


def get_pattern_details(patterns, details):
    pattern = None
    for candidate in patterns:
        if candidate.name == pattern.name and candidate.size == pattern.size and candidate.pattern_type == pattern.pattern_type:
            pattern = candidate
            break
    if pattern is None:
        raise IntegrityError("Выкройка не найдена")

    details_by_pattern = defaultdict(list)
    for detail in details:
        if detail.pattern_id == pattern.name:
            details_by_pattern[pattern.name].append(detail)

    return details_by_pattern[pattern.name]


def verify_details_integrity(patterns, details):
    details_by_pattern = defaultdict(list)
    for detail in details:
        if detail.pattern_id in [p.name for p in patterns]:
            details_by_pattern[detail.pattern_id].append(detail)

    for pattern in patterns:
        if len(details_by_pattern[pattern.name]) == 0:
            raise IntegrityError(
                f"Выкройка '{pattern.name}' не имеет связанных деталей"
            )

    for detail in details:
        if not any(p.name == detail.pattern_id for p in patterns):
            raise IntegrityError(f"Деталь '{detail.name}' ссылается на несуществующую выкройку")


def main():
    patterns = [
        Pattern("Костюм", "Повседневный", "S", "Средняя"),
        Pattern("Платье", "Вечернее", "M", "Сложная"),
    ]
    details = [
        Detail(1, "Перед", "Костюм"),
        Detail(2, "Зад", "Костюм"),
        Detail(3, "Рукав", "Костюм"),
        Detail(4, "Юбка", "Платье"),
        Detail(5, "Верх", "Платье"),
        Detail(6, "Ошибочная", "Отсутствующая"),
    ]

    target = Pattern("Платье", "Вечернее", "M", "Сложная")
    print(get_pattern_details(patterns, details))
    verify_details_integrity(patterns, details)
    print("Целостность проверена успешно")


if __name__ == "__main__":
    main()
