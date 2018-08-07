import datetime
from picamera import PiCamera
from time import sleep

camera = PiCamera()

#camera.start_preview()
#sleep(5)
now = datetime.datetime.now()
camera.capture('/mnt/cameraimages/images/img-' + now.strftime("%Y-%m-%d-%H-%M-%S") + '.jpg')
#camera.stop_preview()
