# === Stage 3: Хранилище в памяти ===
# Project: SewingPatterns
memory_store.py

from typing import Dict, List, Optional


class PatternMemoryStore:
    """Восстановимое в памяти хранилище сущностей «выкройка» по идентификатору."""

    def __init__(self) -> None:
        self._patterns: Dict[str, dict] = {}

    def add(self, pattern_id: str, name: str, pattern_type: str, size: str, difficulty: str) -> None:
        self._patterns[pattern_id] = {
            "pattern_id": pattern_id,
            "name": name,
            "pattern_type": pattern_type,
            "size": size,
            "difficulty": difficulty,
        }

    def get(self, pattern_id: str) -> Optional[dict]:
        return self._patterns.get(pattern_id)

    def list(self) -> List[dict]:
        return list(self._patterns.values())


if __name__ == "__main__":
    store = PatternMemoryStore()

    store.add(
        pattern_id="p-001",
        name="Классическое платье",
        pattern_type="Одежда",
        size="M",
        difficulty="Средняя",
    )
    store.add(
        pattern_id="p-002",
        name="Простой шарф",
        pattern_type="Аксессуар",
        size="O",
        difficulty="Лёгкая",
    )

    print("Добавлено выкроек:", len(store.list()))

    found = store.get("p-001")
    if found:
        print("Получена выкройка:", found["name"], "размер", found["size"])

    print("Список выкроек:")
    for pattern in store.list():
        print(" -", pattern["name"], "(", pattern["pattern_type"], ")")

    missing = store.get("p-999")
    print("Отсутствующая выкройка:", missing)
