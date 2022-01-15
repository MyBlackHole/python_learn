#!/user/bin/env python
# -*- coding: utf-8 -*-


class AlarmSensor:
    def __init__(self):
        self.name = "AlarmSensor"

    def run(self):
        print("Alarm Ring...", self.name)


class WaterSk:
    def __init__(self):
        self.name = "WaterSk"

    def run(self):
        print("Spray Water...", self.name)


class EmergencyDialer:
    def __init__(self):
        self.name = "EmergencyDialer"

    def run(self):
        print("Dial 119...", self.name)


class EmergencyFacade:
    def __init__(self):
        self.alarm_sensor = AlarmSensor()
        self.water_sk = WaterSk()
        self.emergency_dialer = EmergencyDialer()

    def run_all(self):
        self.alarm_sensor.run()
        self.water_sk.run()
        self.emergency_dialer.run()


if __name__ == "__main__":
    emergency_facade = EmergencyFacade()
    emergency_facade.run_all()
