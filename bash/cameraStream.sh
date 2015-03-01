#! /bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/pi/dev/code/bash/cameraStream.sh

	# Switch off +5V camera
	rpio --setoutput 26:0
	sleep 5

	# Take a picture
	/home/pi/dev/code/python/takePic.py
	sleep 2
	
	# Switch on +5V camera
	rpio --setoutput 26:1
	sleep 5

	# Mount the camera
	mount /dev/sdb1 /mnt/camera
	
	# Copy the picture to USB drive 
	cp /mnt/camera/DCIM/100MEDIA/SUNP0001.JPG "/mnt/storage/`date +%d-%m-%Y_%Hh%M`.JPG"

	# Remove the picture from the camera
	rm /mnt/camera/DCIM/100MEDIA/SUNP0001.JPG

	# Unmount the camera
	umount /mnt/camera
