import time

from task_management import Scheduler
from updated_distance import measure_distance_task
from updated_camera import capture_image_task
from updated_led import control_led_task
from updated_classify import capture_and_classify_image_task\

# Initialize the scheduler
scheduler = Scheduler()
scheduler.SCH_Init()

# Add tasks to the scheduler (Example delays and periods, adjust as needed)
# Measure distance every 5 seconds
scheduler.SCH_Add_Task(measure_distance_task, DELAY=0, PERIOD=300000)
# Capture an image every 10 seconds
scheduler.SCH_Add_Task(capture_image_task, DELAY=0, PERIOD=300000)
# Control LED based on light sensor, checked every 3 seconds
scheduler.SCH_Add_Task(control_led_task, DELAY=0, PERIOD=300000)
# Capture and classify an image every 15 seconds
scheduler.SCH_Add_Task(capture_and_classify_image_task, DELAY=0, PERIOD=300000)

# Main loop
while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(100)
