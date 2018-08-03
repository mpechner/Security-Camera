# Security-Camera
Raspberry Pi AWS S3 Backed Security Camera Project


After an odd incident at the house I decided on the need for a securitty camera.  But do not trust these companies not to leak passwords or have the photos leak. I don't walk around naked, not that ANYONE wants to see that, but I'm not 100% covered either.


I figure with a PIR sensor, a Raspbery Pi camera and using a private AWs S3 bucket, I capture the images.


The basic coding of sensing motion with a PIR motion sensor that triggers capturing images or videos with the camera is easy.  Pushing the images to S3 is a nice add.


Since this is a Pi, so not need to use a simple single process.  One process to capture, one to kick off max N push processes.  S3 upload speeds do not saturate most home internet connections.  So push thart data as fast as you can.  Most;y because if someone really does break in, get at leasat. One image uploaded before the person sees and destroys the Pi could make all the difference in the world.  Paranoid much :-D.


I will be testinmg both the bassic and IR camera. Will test PIR as well as ultrasonic.  Lidar wouild be fun, but those are a bit costly.
