# Security-Camera
Raspberry Pi AWS S3 Backed Security Camera Project

Read the wiki https://github.com/mpechner/Security-Camera/wiki

# Why and What
After an odd incident at the house I decided on the need for a security camera.  But do not trust these companies not to leak passwords or have the photos leak. I don't walk around naked, not that ANYONE wants to see that, but I'm not 100% covered either.


With a PIR sensor, a Raspbery Pi camera and using a private AWS S3 bucket, I capture the images. And haver 100% control.  Since I only care to look at the images if soemthing happens, not going to write something that makes the images generaly available.


The basic coding of sensing motion with a PIR motion sensor that triggers capturing images or videos with the camera is easy.  Pushing the images to S3 is a nice add.

I will be testing both the bassic and IR camera. Will test PIR as well as ultrasonic.  Lidar wouild be fun, but those are a bit costly and not sure the Pi has the power to make it go.

![Prototype](https://github.com/mpechner/Security-Camera/wiki/images/prototype.jpg)

# Fast & Dirty for the impatient and knowledgeable
* setup AWS Credentials
* PIR output is off pin 11 by default.
* enable the camera
* copy security-camera.py where you want it.  Make it executable.
* copy security-camera.service to /etc/systemd/system.  Edit it to point your S3 bucket. enable, start, reload.

# First Pass 8/5/2018
Prototype Done.  Probably spent more time working on the wiki than coding.  I did waste time not knowing the Pi IR camera has a different setup. My first systemd service.  I'm an old school init.d guy.  AWS Linux has not forced the issue yet and I still have most Centos 6 systems.

Still prototype.  I have not soldiered or encased anything yet.

# Second Pass 10/12/2020 on branch VC0706
* On branch vc0706 I switched to the adafruit jpeg camera, https://www.adafruit.com/product/613.
* I moved from python2 to python3
* Will need to "sudo pip3 install adafruit-circuitpython-vc0706"
* Code is based on https://circuitpython.readthedocs.io/projects/vc0706/en/latest/examples.html
* Also since I connected the rx/tx to the GPIO pins, set "enable_uart=1" in /boot/config.txt/
