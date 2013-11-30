# uncomment the following lines to enable visual studio remote debugging
#import ptvsd
#ptvsd.enable_attach(secret = 'vs2013')

import RPi.GPIO as GPIO
import threading
import sys
import select
from azure.servicebus import *
import os

# Make sure you set the following:
AZURE_SERVICEBUS_NAMESPACE=''
# Note: the user needs to have access to manage the servicebus
AZURE_SERVICEBUS_ISSUER=''
AZURE_SERVICEBUS_ACCESS_KEY=''

def process_messages():
    # Initialize the service bus
    bus_service = ServiceBusService(AZURE_SERVICEBUS_NAMESPACE,account_key=AZURE_SERVICEBUS_ACCESS_KEY,issuer=AZURE_SERVICEBUS_ISSUER)
    bus_service.create_topic("blinky")
    bus_service.create_subscription("blinky","AllMessages")
    while True:
      msg = bus_service.receive_subscription_message('blinky', 'AllMessages', peek_lock=False)
      if msg.body is not None:
        print(msg.body)
        if msg.custom_properties["led"]==1:
            print("turning on the LED")
            GPIO.output(11, 1)
        else:
            print("turning off the LED")
            GPIO.output(11, 0)

# setup the GPIO for the LED
GPIO.setmode(GPIO.BCM)
GPIO.setup(11,GPIO.OUT)

# Initially turn off the LED
GPIO.output(11, 0)

# start a thread listening for incomming messages
t = threading.Thread(target=process_messages)
t.daemon=True;
t.start()

# pause until the user enters something
char = raw_input("Press enter to exit program")

# release any GPIO resources
GPIO.cleanup()
