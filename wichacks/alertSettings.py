from dataclasses import dataclass
from wichacks import alertType

@dataclass
class Settings:
    name: str  # name of alert
    alert_type: alertType.Type  # type fo alert e.g. health, hygiene
    alert_time: int  # alert time
    enabled: bool  # whether the alert is enabled


def create_alert(name, type, time, enable):
    """
    Constructor for Settings
    :param name: name of alert
    :param type: type of alert
    :param time: time alert goes off
    :param enable: whether alert is set to go off
    :return: New settings object
    """
    Settings.alert_type = type
    return Settings(name, type, time, enable)


def set_name(name):
    """
    Rename alert
    :param name: name of the alert
    :return: None
    """
    Settings.name = name


def set_type(type):
    """
    Reset type of alert
    :param type: the type the alert is being changed with
    :return: None
    """
    Settings.alert_type = alertType.set_type(type)


def set_time(time):
    """
    Reset time the alert will go off
    :param time: Time for the alert
    :return: None
    """
    Settings.alert_time = time


def set_enabled(state):
    """
    Change if the alert is selected to go off
    :param state: true or false
    :return: None
    """
    Settings.enabled = state


def get_name():
    """
    Get name of the alert
    :return: the name
    """
    return Settings.name


def get_type():
    """
    Get the type of the alert
    :return: the type
    """
    return Settings.alert_type


def get_time():
    """
    Get what time the alert goes off
    :return: the time
    """
    return Settings.alert_time


def get_enabled():
    """
    Get whether the alert is set to go off
    :return: true if the alert will go off, false if not
    """
    return Settings.enabled

