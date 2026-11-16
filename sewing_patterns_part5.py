# === Stage 5: Удаление и восстановление ===
# Project: SewingPatterns
import time


class SoftDeleteMixin:
    is_deleted = False
    deleted_at = None

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = time.time()

    def restore(self):
        if self.is_deleted:
            self.is_deleted = False
            self.deleted_at = None
            return True
        return False


class PatternRepository:
    def __init__(self):
        self._items = {}

    def add(self, pattern):
        self._items[pattern.id] = pattern

    def get(self, pattern_id):
        return self._items.get(pattern_id)

    def delete(self, pattern_id):
        pattern = self._items.pop(pattern_id, None)
        if pattern is None:
            return False
        pattern.soft_delete()
        return True

    def get_active(self, pattern_id):
        pattern = self._items.get(pattern_id)
        if pattern is None:
            return None
        if pattern.is_deleted:
            return None
        return pattern

    def list_active(self):
        return [p for p in self._items.values() if not p.is_deleted]

    def list_deleted(self):
        return [p for p in self._items.values() if p.is_deleted]

    def restore(self, pattern_id):
        pattern = self._items.get(pattern_id)
        if pattern is None or not pattern.is_deleted:
            return False
        pattern.restore()
        return True

    def clear_deleted(self):
        deleted = [p for p in self._items.values() if p.is_deleted]
        for pattern in deleted:
            self._items.pop(pattern.id, None)
        return deleted


if __name__ == "__main__":
    repo = PatternRepository()
    pattern = SoftDeleteMixin()
    pattern.id = "p1"
    pattern.name = "Dress"
    pattern.type = "garment"
    pattern.size = "M"
    pattern.difficulty = "medium"
    repo.add(pattern)

    repo.delete("p1")
    print("active:", repo.get_active("p1"))
    print("deleted:", repo.list_deleted())
    repo.restore("p1")
    print("active:", repo.get_active("p1"))
    print("deleted:", repo.list_deleted())
