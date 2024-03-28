
from task_management import Task, Scheduler
from counterfit_connection import CounterFitConnection
import io
from counterfit_shims_picamera import PiCamera
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from counterfit_shims_grove.grove_led import GroveLed 
# Initialize CounterFit Connection
CounterFitConnection.init('127.0.0.1', 5000)
led = GroveLed(5)
# Task function to capture and classify an image
def capture_and_classify_image_task():
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.rotation = 0

    image = io.BytesIO()
    camera.capture(image, 'jpeg')
    image.seek(0)

    with open('image.jpg', 'wb') as image_file:
        image_file.write(image.read())

    # Replace these with your own Azure Custom Vision details
    prediction_url = ''
    prediction_key = ''
    project_id = ''
    iteration_name = 'Iteration6'
    

    prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
    predictor = CustomVisionPredictionClient(prediction_url, prediction_credentials)

    image.seek(0)
    results = predictor.classify_image(project_id, iteration_name, image)

    for prediction in results.predictions:
        print(f'{prediction.tag_name}: {prediction.probability * 100:.2f}%')
        if prediction.tag_name in ['Unripe tomatoes', 'Rotten tomatoes']:
            print("Tomato is not ripe. Turning on LED.")
            led.on()
            break  # Assuming you only need to process the most confident prediction
        else:
            print("Tomato is ripe. Turning off LED.")
            led.off()
            break

    
        
        

