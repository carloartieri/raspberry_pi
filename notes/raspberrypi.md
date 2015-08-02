#Raspberry Pi	Notes

##Scenarios

###Setting up external storage

To easily **format external drives and work with partitions**, you can install **gparted** with:

		sudo apt-get install gpart gparted
	
The partition manager can then be run from the terminal within the graphical environment by typing:
	
		xhost +
		sudo gparted

Find the external drive in the drop-down menu, unmount it (if mounted), and format it in **ext4** format.

Reboot the Raspberri Pi and run gparted again, noting the path to the partition (probably /dev/sda1).

Create a directory where the external drive will be mounted such as:

	sudo mkdir /mnt/externalstorage

Then add the following line to the /etc/fstab file, replacing the first and second entries with the appropriate values:

	sudo vim /etc/fstab

	/dev/sda1       /mnt/externalstorage    ext4    defaults        0       0

The drive should now mount automatically when the Pi reboots, but you can also mount/unmount it directly with:

	sudo mount -a						#Mounts all according to /etc/fstab
	sudo umount /mnt/externalstorage	#Unmount the external drive
	
	
	
##Software/Packages

###Unicorn HAT

With python-pip and python-dev installed, run:

	sudo pip install unicornhat

Also get the Unicorn HAT examples and documentation from GitHub with:

	git clone https://github.com/pimoroni/unicorn-hat

Function reference [here](https://github.com/pimoroni/unicorn-hat/blob/master/documentation/Function-reference.md).

</br>
###Munin

[Munin](http://guide.munin-monitoring.org/en/latest/index.html) is a networked resource monitoring tool that allows you to monitor your system's performance (including temperature and voltage) via a web interface.

	sudo apt-get install munin munin-node lighttpd

In order to view the graphs that munin produces, we install [lighttpd](http://www.lighttpd.net/), a low-ressource, flexible web server. We have to link the data produced by munin to the web server.

	sudo ln -s /var/cache/munin/www/ /var/www/munin
	
In order to get data from the Pi's temperature, voltage, and frequency sensors, we have to install the Pisense module.

	cd /usr/share/munin/plugins
	sudo wget https://raw.githubusercontent.com/perception101/pisense/master/pisense_
	sudo chown root:root pisense_
	sudo chmod 755 pisense_
	
The user won't have the rights to read the temperature. So edit the following file and add the lines below:

	sudo vim /etc/munin/plugin-conf.d/pisense
	
	[pisense_*]
	user root

Finally, you must activate the pisense module, by setting up the following symlinks, followed by restarting munin.

	sudo ln -s /usr/share/munin/plugins/pisense_ /etc/munin/plugins/pisense_temp
	sudo ln -s /usr/share/munin/plugins/pisense_ /etc/munin/plugins/pisense_clock
	sudo ln -s /usr/share/munin/plugins/pisense_ /etc/munin/plugins/pisense_volt

	sudo service munin-node restart

You should now be able to view Munin's charts on your local network by accessing http://<Raspberry Pi IP>/munin/
