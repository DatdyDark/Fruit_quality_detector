
from task_management import Task, Scheduler
import time
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed

# Initialize CounterFit Connection
CounterFitConnection.init('127.0.0.1', 5000)

# Task function to control LED based on light sensor reading
def control_led_task():
    light_sensor = GroveLightSensor(0)
    led = GroveLed(5)
    light = light_sensor.light
    print('Light level:', light)
    if light < 300:
        led.on()
    else:
        led.off()

# This function should be scheduled in the main system's scheduler
