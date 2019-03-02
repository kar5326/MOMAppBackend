from dataclasses import dataclass
from wichacks import alert_type

@dataclass
class Settings:
    name: str  # name of alert
    alert_type: alert_type.Type  # type fo alert e.g. health, hygiene
    alert_time: int  # alert time
    enabled: bool  # whether the alert is enabled


def create_alert(name, type, time, enable):
    #  Settings.name = name
    Settings.alert_type = type
    #  Settings.alert_time = time
    #  Settings.enabled = enable
    return Settings(name, type, time, enable)

