# === Stage 6: Связанная сущность ===
# Project: SewingPatterns
class PatternDetail:
    def __init__(self, name, pattern_id, quantity, fabric_type, cut_length):
        self.name = name
        self.pattern_id = pattern_id
        self.quantity = quantity
        self.fabric_type = fabric_type
        self.cut_length = cut_length

    def to_dict(self):
        return {
            "name": self.name,
            "pattern_id": self.pattern_id,
            "quantity": self.quantity,
            "fabric_type": self.fabric_type,
            "cut_length": self.cut_length,
        }


class PatternLibrary:
    def __init__(self):
        self._details = {}

    def add_detail(self, name, pattern_id, quantity, fabric_type, cut_length):
        detail = PatternDetail(
            name=name,
            pattern_id=pattern_id,
            quantity=quantity,
            fabric_type=fabric_type,
            cut_length=cut_length,
        )
        self._details[pattern_id] = self._details.get(pattern_id, 0) + [detail]
        return detail

    def get_details(self, pattern_id):
        return list(self._details.get(pattern_id, []))
