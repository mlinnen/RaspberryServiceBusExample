Raspberry PI Service Bus Example
==========================

A sample python solution to turn on/off an LED hooked up to the Raspberry PI using the Azure Service Bus. 

* pub_led.py - sends a message to the Raspberry PI via the Azure Service Bus
* sub_led.py - subscribes to the Azure Service Bus looking for a message and turns an LED on/off

**Setup**

Make sure you set the `AZURE_*` variables in both python scripts (sub_led.py and pub_led.py) based on your Service Bus connection information.

Setup the raspberry pi for Python development:

	sudo apt-get install python-dev
	curl -O http://python-distribute.org/distribute_setup.py
	python distribute_setup.py
	curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
	python get-pip.py
	sudo pip install virtualenv
	pip install rpi.gpio
    
Install the Azure Python SDK:

	sudo pip-2.7 install azure

