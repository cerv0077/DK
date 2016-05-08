import time, math
from dronekit import connect, VehicleMode, LocationGlobalRelative, GPSInfo
from pymavlink import mavutil


import argparse  
parser = argparse.ArgumentParser(description='Commands vehicle using vehicle.simple_goto.')
parser.add_argument('--connect', 
                   help="Vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

connection_string = args.connect
sitl = None

if not args.connect:
	print "Starting copter simulator (SITL)"
	from dronekit_sitl import SITL
	sitl = SITL()
	sitl.download('copter', '3.3', verbose=True)
	sitl_args = ['-I0', '--model', 'quad', '--home=49.061874,17.198439,584,353']
	sitl.launch(sitl_args, await_ready=True, restart=True)
	connection_string = 'tcp:127.0.0.1:5760'



# Connect to the Vehicle (SITL)
print 'Connecting to vehicle on: %s' % connection_string
vehicle = connect(connection_string, wait_ready=True)

update_rate = 0.02 


while True:
	current = time.time()
	elapsed = 0

	print 'GPS lat', vehicle.location.global_relative_frame.lat
	print 'GPS long', vehicle.location.global_relative_frame.lon
	print 'Altitude global frame', vehicle.location.global_frame.alt
	print 'Altitude global relative frame',vehicle.location.global_relative_frame.alt
	print 'attitude', vehicle.attitude #SR2_EXTRA1
	print 'heading', vehicle.heading



	while elapsed < update_rate:
		elapsed = time.time() - current




vehicle.close