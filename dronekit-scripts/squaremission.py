import collections
import collections.abc
collections.MutableMapping = collections.abc.MutableMapping
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time 
#step 1 is to connect the drone with Ardupilot simulator
print("connecting the drone ")
vehicle=connect('udp:127.0.0.1:14552',wait_ready=True)
#step 2 is to run pre-arming checks 
print("running pre-arming checks on the drone")
while not vehicle.is_armable:
    print("waiting for gps to lock")
    time.sleep(1)
#step 3 is to arm the vehicle
print("arming the motors of the vehicle")
vehicle.mode=VehicleMode("GUIDED")
vehicle.armed=True
while not vehicle.armed:
    time.sleep(1)
#step4:take off
print("taking off to 10m")
vehicle.simple_takeoff(10)
while True:
    alt=vehicle.location.global_relative_frame.alt
    print(f"Alt: {alt:.1f}m")
    if  alt>=9.5:
        print("altitude reached")
        break
    time.sleep(1)
#step 5 is now moving to locations
#airspeed is how fast vehicle flies in air 
# ==========================================
# STEP 5: THE WAYPOINT MISSION
# ==========================================
vehicle.airspeed = 5 

print("--> Flying to Waypoint 1 (20m North)")
wp1 = LocationGlobalRelative(-35.363082, 149.165230, 10)
vehicle.simple_goto(wp1)
time.sleep(15) 

print("--> Flying to Waypoint 2 (20m East)")
wp2 = LocationGlobalRelative(-35.363082, 149.165450, 10)
vehicle.simple_goto(wp2)
time.sleep(15)

print("--> Flying to Waypoint 3 (20m South)")
wp3 = LocationGlobalRelative(-35.363261, 149.165450, 10)
vehicle.simple_goto(wp3)
time.sleep(15)

print("--> Flying to Waypoint 4 (20m West - Back to Start)")
wp4 = LocationGlobalRelative(-35.363261, 149.165230, 10)
vehicle.simple_goto(wp4)
time.sleep(15)
# ==========================================

#step6:Return to launch
print("returning to launch pad")
vehicle.mode=VehicleMode("RTL")
while vehicle.armed:
    print("descending")
    time.sleep(2)
print("vehicle landed")
vehicle.close()    



    