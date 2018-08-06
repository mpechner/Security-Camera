import boto3
import os
import datetime
from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--awsprofile", default="default", help="profile from ~/.aws/credentials to use")
parser.add_argument("--cameraname", default="camera1", help="name the camera, files will be uploaded to a folder containing this name")
parser.add_argument("--bucket", default="mikey.com-security", help="S3 bucket name")
parser.add_argument("--imagepath", default="/mnt/cameraimages/images", help="locatioon where images are to be written")
args = parser.parse_args()

cameraname=args.cameraname
bucket=args.bucket
imagepath=args.imagepath

def upload():
    s3 = boto3.resource('s3')
    for dirName, subdirList, fileList in os.walk(imagepath):
        for fname in fileList:
            if len(imagepath) == len(dirName):
                finame=fname
            else:
                finame = '%s/%s'%(dirName[len(imagepath)+1:], fname)
            #print(finame)
            res=s3.meta.client.upload_file(dirName + '/' + fname, bucket, finame)
            os.unlink(dirName + '/' + fname)

def capture():
    now = datetime.datetime.now()
    camera.capture('/mnt/cameraimages/images/'+ cameraname  +'/img-' + now.strftime("%Y-%m-%d-%H-%M-%S") + '.jpg')

def waitfor():
    # Based on https://maker.pro/raspberry-pi/tutorial/how-to-interface-a-pir-motion-sensor-with-raspberry-pi-gpio
    # just seeing that the PIR works.
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
    while True:
        i=GPIO.input(11)
        if i==0:                 #When output from motion sensor is LOW
            time.sleep(0.5)
        elif i==1:               #When output from motion sensor is HIGH
            print "Intruder detected",i
            capture()
            upload()
            time.sleep(0.3)


camera = PiCamera()

if not os.path.exists(imagepath + '/' + cameraname):
    os.makedirs(imagepath + '/' + cameraname, 0777)
waitfor()
