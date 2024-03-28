
from task_management import Task, Scheduler
from counterfit_connection import CounterFitConnection
import time
from counterfit_shims_rpi_vl53l0x.vl53l0x import VL53L0X

# Initialize CounterFit Connection
CounterFitConnection.init('127.0.0.1', 5000)

# Task function to measure distance
def measure_distance_task():
    distance_sensor = VL53L0X()
    distance_sensor.begin()
    distance_sensor.wait_ready()
    print(f'Distance = {distance_sensor.get_distance()} mm')

# Assuming this is part of a larger system where the scheduler is initialized elsewhere
# and tasks are added in a main.py or similar entry point
