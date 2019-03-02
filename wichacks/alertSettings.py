from dataclasses import dataclass


@dataclass
class Type:
    HEALTH = 1
    EATING = 2
    SCHEDULE = 3
    EXTRA = 4

@dataclass
class Settings:
    name: str
    type: Type
    alert_time: int
    enabled: bool

