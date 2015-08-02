#Raspberry Pi	Stuff

Scripts and files for use on my Raspberry Pi.

Directory | Notes
:---|:---
notes/| General notes I've made about working with the Pi 
unicorn_hat/| Controlling the [Pimoroni](http://shop.pimoroni.com/) [Unicorn HAT](http://shop.pimoroni.com/products/unicorn-hat)

</br>
##Installing the Raspbian OS to an SD Card (OS X)

1. Download the latest version of Raspbian from [https://www.raspberrypi.org/downloads/](https://www.raspberrypi.org/downloads/)
2. Plug in the SD Card and launch the OS X Disk Utility. 
3. Select the SD Card and erase its contents, formatting to MS-DOS (FAT)
4. Click the info button and note the 'Disk Indentifier' (i.e. 'disk#')
5. Right click on the newly formatted partition and select 'unmount'
6. Open a terminal window and run the following, replacing 'diskn' with the Disk Identifier, noted above:

		sudo dd bs=32m if=path_of_your_image.img of=/dev/diskn 

This should take ~30 mins to an hour. Once finished, eject the SD card and plug it into the Pi before connecting the system to a power source.

##Initialization
Upon reinstalling Raspian on the Pi, you should update all packages and install the following software:

	sudo apt-get update
	sudo apt-get upgrade
	
	sudo apt-get install vim			Get vim text editor
	sudo apt-get install python-pip		Get pip for Python 2.0 packages
	sudo apt-get install python-dev		Get dev libraries for Python
	

###Specific issues:

1. To get a full screen display, edit the **/boot/config.txt** file to make sure that the **disable_overscan** setting is uncommented and set to 1.
		
		disable_overscan=1

2. Mouse movement in the Raspian desktop environment is sluggish, which can be fixed by integrating the following option into the single command line in the file **/boot/cmdline.txt**, separated by spaces:

		usbhid.mousepoll=0

3. If you've ever accidentally configured the Pi to boot into **scratch**, press **CONTROL+ALT+F2** to access a terminal and rerun the configuration menu with **sudo raspi-config**, choosing another boot option.

</br>
##Basic tools/commands

Critical shell commands:

	sudo reboot 					Reboot the Pi
	sudo shutdown -h now			Shutdown the Pi
	
	sudo raspi-config				Initialize the configuration menu
	
	startx							Launch the GUI

	ip addr show 					Show the Pi's IP address

	vcgencmd [command]				Get physical statistics from Pi
		measure_temp				Get temperature (°C)
		measure_volts				Get voltage 
		vcgencmd measure_clock arm	Get processor freq in Hz