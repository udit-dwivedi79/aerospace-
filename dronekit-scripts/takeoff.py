 #THE  FIX FOR PYTHON 3.10 ---
import collections
import collections.abc
collections.MutableMapping = collections.abc.MutableMapping
# -----------------------------------
from dronekit import connect , VehicleMode 
import time 
#step 1 :connect
print("connecting to drone")
vehicle=connect('udp:127.0.0.1:14552',wait_ready=True)
#step 2 pre arm checks 
print("running pre-arm checks")
while not vehicle.is_armable:
  print("waiting for gps lock...")
  time.sleep(1)
#step 3 arming the motors
print("arming the motors")
vehicle.mode=VehicleMode("GUIDED")
vehicle.armed=True
while not vehicle.armed:
    print("Waiting for vehicle to arm")
    time.sleep(1)
#step 4 take off 
target_altitude=10
print(f"taking off to {target_altitude} meters")
vehicle.simple_takeoff(target_altitude)
#monitor flight while it climbs
while True:
    current_altitude=vehicle.location.global_relative_frame.alt
    current_heading=vehicle.heading
    current_airspeed=vehicle.airspeed
    print(f"Alt:{current_altitude: .1f}m | heading: {current_heading} | Airspeed:{current_airspeed:.1f}m/s")
    #if we reach 9.5meters ,stop the loop 
    if current_altitude>=target_altitude*0.95:
        print("target altitude reachedd")
        break
        time.sleep(1)
print("hovering for 5 seconds")
time.sleep(5)
#step5:RTL(Return to launch)
print("mission complete returning to launch")
vehicle.mode=VehicleMode("RTL")
#wait for the drone to land before disconnecting 
while vehicle.armed:
    print("descending")
    time.sleep(2)
print("drone has landed and disarmed disconnecting")
vehicle.close()

