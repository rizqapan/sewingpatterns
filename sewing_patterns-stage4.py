# === Stage 4: Редактирование записей ===
# Project: SewingPatterns
from typing import Any, Dict, Optional


class PatternEditor:
    """Редактор сущности «выкройка» с валидацией допустимых полей."""

    ALLOWED_FIELDS = {"name", "type", "size", "difficulty"}

    def __init__(self, original: Dict[str, Any]) -> None:
        self._original = dict(original)

    def update(self, id: Any, changes: Dict[str, Any]) -> Dict[str, Any]:
        if id not in self._original:
            raise KeyError(f"Выкройка с идентификатором {id} не найдена")

        allowed = self.ALLOWED_FIELDS & set(changes.keys())
        unknown = set(changes.keys()) - self.ALLOWED_FIELDS
        if unknown:
            raise ValueError(
                f"Недопустимые поля для изменения: {', '.join(sorted(unknown))}"
            )

        updated = dict(self._original)
        for key, value in changes.items():
            updated[key] = value

        return updated


def patch_pattern(pattern: Dict[str, Any], changes: Dict[str, Any]) -> Dict[str, Any]:
    """Применить частичные изменения к выкройке с проверкой полей."""
    editor = PatternEditor(pattern)
    return editor.update(None, changes)
