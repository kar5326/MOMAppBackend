from dataclasses import dataclass


@dataclass
class Type:
    HEALTH = 1
    EATING = 2
    SCHEDULE = 3
    EXTRA = 4


def set_type(type):
    Type = type
    return Type
