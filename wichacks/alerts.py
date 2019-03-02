from wichacks import alertSettings
from wichacks import alertType


def sleep():
    alertSettings.create_alert("Sleep", alertType.set_type(alertType.Type.HEALTH), 2000, True)


def hygiene():
    alertSettings.create_alert("Hygiene", alertType.set_type(alertType.Type.HEALTH), 2000, True)


def exercise():
    alertSettings.create_alert("Exercise", alertType.set_type(alertType.Type.HEALTH), 2000, True)


def drink():
    alertSettings.create_alert("Drink Water", alertType.set_type(alertType.Type.EATING), 2000, True)


def make_food():
    alertSettings.create_alert("Cook Dinner", alertType.set_type(alertType.Type.HEALTH), 2000, True)


def shopping():
    alertSettings.create_alert("Shopping List", alertType.set_type(alertType.Type.EATING), 2000, True)


def recipe():
    alertSettings.create_alert("Daily Recipe", alertType.set_type(alertType.Type.EATING), 2000, True)


def calendar():
    alertSettings.create_alert("Calendar", alertType.set_type(alertType.Type.SCHEDULE), 2000, True)


def work():
    alertSettings.create_alert("Work Schedule", alertType.set_type(alertType.Type.SCHEDULE), 2000, True)


def encouragement():
    alertSettings.create_alert("Encouragement", alertType.set_type(alertType.Type.EXTRA), 2000, True)


def phone_time():
    alertSettings.create_alert("Phone Time", alertType.set_type(alertType.Type.EXTRA), 2000, True)
