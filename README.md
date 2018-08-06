# Security-Camera
Raspberry Pi AWS S3 Backed Security Camera Project

# Why and What
After an odd incident at the house I decided on the need for a security camera.  But do not trust these companies not to leak passwords or have the photos leak. I don't walk around naked, not that ANYONE wants to see that, but I'm not 100% covered either.


With a PIR sensor, a Raspbery Pi camera and using a private AWS S3 bucket, I capture the images. And haver 100% control.  Since I only care to look at the images if soemthing happens, not going to write something that makes the images generaly available.


The basic coding of sensing motion with a PIR motion sensor that triggers capturing images or videos with the camera is easy.  Pushing the images to S3 is a nice add.

I will be testinmg both the bassic and IR camera. Will test PIR as well as ultrasonic.  Lidar wouild be fun, but those are a bit costly and not sure the Pi has the power to make it go.

![Prototype](https://github.com/mpechner/Security-Camera/wiki/images/prototype.jpg)

# First Pass 8/5/2018
Prototype Done.  Probably spent more time working on the wiki than coding.  I did waste time not knowing the Pi IR camera has a different setup. My first systemd service.  I'm an old school init.d guy.  AWS Linux has not forced the issue yet and I still have most Centos 6 systems.

Still prototype.  I have not soldiered or encased anything yet.
