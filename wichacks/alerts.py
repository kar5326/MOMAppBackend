from wichacks import alertSettings
from wichacks import alert_type


def sleep():
    alertSettings.create_alert("Sleep", alert_type.set_type(alert_type.Type.HEALTH), 2000, True)
    print(alert_type.set_type(alert_type.Type.HEALTH))


def hygiene():
    alertSettings.create_alert("Hygiene", alert_type.set_type(alert_type.Type.HEALTH), 2000, True)


def exercise():
    alertSettings.create_alert("Exercise", alert_type.set_type(alert_type.Type.HEALTH), 2000, True)


def drink():
    alertSettings.create_alert("Drink Water", alert_type.set_type(alert_type.Type.EATING), 2000, True)


def make_food():
    alertSettings.create_alert("Cook Dinner", alert_type.set_type(alert_type.Type.HEALTH), 2000, True)


def shopping():
    alertSettings.create_alert("Shopping List", alert_type.set_type(alert_type.Type.EATING), 2000, True)


def recipe():
    alertSettings.create_alert("Daily Recipe", alert_type.set_type(alert_type.Type.EATING), 2000, True)


def calendar():
    alertSettings.create_alert("Calendar", alert_type.set_type(alert_type.Type.SCHEDULE), 2000, True)


def work():
    alertSettings.create_alert("Work Schedule", alert_type.set_type(alert_type.Type.SCHEDULE), 2000, True)


def encouragement():
    alertSettings.create_alert("Encouragement", alert_type.set_type(alert_type.Type.EXTRA), 2000, True)


def phone_time():
    alertSettings.create_alert("Phone Time", alert_type.set_type(alert_type.Type.EXTRA), 2000, True)
