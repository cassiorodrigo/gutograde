from dataclasses import dataclass


@dataclass(frozen=True)
class Aluno:
    name: str
    grade: float
    passed: bool
