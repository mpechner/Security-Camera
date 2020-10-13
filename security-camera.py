#!/usr/bin/env python
import boto3
import os
import datetime
#from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import time
import argparse
import adafruit_vc0706
import serial

parser = argparse.ArgumentParser()
parser.add_argument("--cameraname", default="camera1", help="name the camera, files will be uploaded to a folder containing this name")
parser.add_argument("--bucket", required=True, help="S3 bucket name. Required")
parser.add_argument("--imagepath", default="/mnt/cameraimages/images", help="locatioon where images are to be written")
args = parser.parse_args()

cameraname=args.cameraname
bucket=args.bucket
imagepath=args.imagepath

# GPIO setup 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor

# init camera
uart = serial.Serial("/dev/ttyS0", baudrate=115200,timeout=0.50)
# Setup VC0706 camera
vc0706 = adafruit_vc0706.VC0706(uart)
vc0706.baudrate = 115200

# Set the image size.
vc0706.image_size = adafruit_vc0706.IMAGE_SIZE_640x480
size = vc0706.image_size

# make sure initial path exists
if not os.path.exists(imagepath + '/' + cameraname):
    os.makedirs(imagepath + '/' + cameraname, mode=0o777)

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
    
    IMAGE_FILE = '/mnt/cameraimages/images/'+ cameraname  +'/img-' + now.strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
    if not vc0706.take_picture():
        raise RuntimeError("Failed to take picture!")
    # Print size of picture in bytes.
    frame_length = vc0706.frame_length

    # Open a file for writing (overwriting it if necessary).
    # This will write 50 bytes at a time using a small buffer.
    # You MUST keep the buffer size under 100!
    print("Writing image: {}".format(IMAGE_FILE), end="", flush=True)
    stamp = time.monotonic()
    # Pylint doesn't like the wcount variable being lowercase, but uppercase makes less sense
    # pylint: disable=invalid-name
    with open(IMAGE_FILE, "wb") as outfile:
        wcount = 0
        while frame_length > 0:
            t = time.monotonic()
            # Compute how much data is left to read as the lesser of remaining bytes
            # or the copy buffer size (32 bytes at a time).  Buffer size MUST be
            # a multiple of 4 and under 100.  Stick with 32!
            to_read = min(frame_length, 32)
            copy_buffer = bytearray(to_read)
            # Read picture data into the copy buffer.
            if vc0706.read_picture_into(copy_buffer) == 0:
                raise RuntimeError("Failed to read picture frame data!")
            # Write the data to SD card file and decrement remaining bytes.
            outfile.write(copy_buffer)
            frame_length -= 32
            # Print a dot every 2k bytes to show progress.
            wcount += 1
            if wcount >= 64:
                print(".", end="", flush=True)
                wcount = 0
        print('')



def waitfor():
    # Based on https://maker.pro/raspberry-pi/tutorial/how-to-interface-a-pir-motion-sensor-with-raspberry-pi-gpio
    # just seeing that the PIR works.
    
    while True:
        i=GPIO.input(11)
        if i==0:                 #When output from motion sensor is LOW
            time.sleep(0.5)
        elif i==1:               #When output from motion sensor is HIGH
            #print "Intruder detected",i
            capture()
            upload()
            time.sleep(0.3)

waitfor()
