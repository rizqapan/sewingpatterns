# === Stage 1: Каркас модуля ===
# Project: SewingPatterns
from dataclasses import dataclass


@dataclass
class Pattern:
    name: str
    kind: str
    size: str
    difficulty: str


def create_demo_patterns() -> list[Pattern]:
    return [
        Pattern("Джинсы", "основной", "S", "легкий"),
        Pattern("Платье", "основной", "M", "средний"),
        Pattern("Куртка", "основной", "L", "средний"),
        Pattern("Салфетка", "декоративный", "M", "сложный"),
        Pattern("Оборка", "декоративный", "M", "средний"),
    ]


def main() -> None:
    patterns = create_demo_patterns()
    print("Библиотека выкроек SewingPatterns")
    print("=" * 30)
    for pattern in patterns:
        print(f"{pattern.name} | {pattern.kind} | {pattern.size} | {pattern.difficulty}")
    print(f"Всего выкроек: {len(patterns)}")


if __name__ == "__main__":
    main()
