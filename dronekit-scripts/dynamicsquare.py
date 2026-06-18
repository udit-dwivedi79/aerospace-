import collections
import collections.abc
collections.MutableMapping = collections.abc.MutableMapping
from dronekit import connect, VehicleMode,LocationGlobalRelative
import math 
import time
def location_getter(original_latitude,original_longitude,Dnorth,Deast):
    earth_radius=6378137
    Delta_latitude=(Dnorth/earth_radius)*180/math.pi#multiplication with 180/pi to convert rads to degree
    new_latitude=original_latitude+Delta_latitude #assuming original latitude is in degree
    new_latitude_in_radians=new_latitude*(math.pi/180)#this is for cos function of longitude
    Delta_longitude=(Deast/(earth_radius*math.cos(new_latitude_in_radians)))*180/math.pi
    new_longitude=Delta_longitude+original_longitude
    return new_latitude,new_longitude
    #========================================================================================
def distance_meters(location1,location2):     
    current_lat=location1.lat
    current_lon=location1.lon
    target_lat=location2.lat
    target_lon=location2.lon
    dlat=target_lat-current_lat
    current_lat_inrads=math.radians(current_lat)
    dlon=(target_lon-current_lon)*math.cos(current_lat_inrads)
    distance= (((dlat)**2+(dlon)**2)**0.5)*1.113195*10**5
    return distance 
    #==========================================================================================
    #making the loop to pause the pythin script
#step 1 connecting the drone
print("connecting the drone with the SITL")
vehicle=connect('udp:127.0.0.1:14552',wait_ready=True)
#step2 performing pre_arming checks
while not vehicle.is_armable:
    print("waiting for the gps to lock")
    time.sleep(1)
#step 3 arming the drone
vehicle.mode=VehicleMode("GUIDED")
vehicle.armed=True
while not vehicle.armed:
    print("arming the vehicles")
    time.sleep(1)
#step 4 take off     
print("taking off")
vehicle.simple_takeoff(10)
while True:
    alt=vehicle.location.global_relative_frame.alt
    print(f"ascending in altitude current altitude is:{alt} meters")
    if alt>=9.5:
     print("we have reached the altitude")
     break
    time.sleep(1) 
start_loc=vehicle.location.global_relative_frame
wp1_lat,wp1_lon=location_getter(start_loc.lat,start_loc.lon,20,0)
wp1=LocationGlobalRelative(wp1_lat,wp1_lon,10)
vehicle.simple_goto(wp1)
while True:
    current_location=vehicle.location.global_relative_frame
    dist=distance_meters(current_location,wp1)
    print(f"the current distance from the target location {wp1} is {dist} meters")
    if dist<=1:
        print("we have arrived at location 1")
        break
    else: time.sleep(1)
    #========================================================================================  
wp2_lat,wp2_lon=location_getter(wp1_lat,wp1_lon,0,20)
wp2=LocationGlobalRelative(wp2_lat,wp2_lon,10)
vehicle.simple_goto(wp2)
while True:
    current_location=vehicle.location.global_relative_frame
    dist=distance_meters(current_location,wp2)
    print(f"the current distance from the target location {wp2} is {dist} meters")
    if dist<=1:
        print("we have arrived at location 2")
        break
    else: time.sleep(1)
    #==========================================================================================
wp3_lat,wp3_lon=location_getter(wp2_lat,wp2_lon,-20,0)
wp3=LocationGlobalRelative(wp3_lat,wp3_lon,10)
vehicle.simple_goto(wp3)
while True:
    current_location=vehicle.location.global_relative_frame
    dist=distance_meters(current_location,wp3)
    print(f"the current distance from the target location {wp3} is {dist} meters")
    if dist<=1:
        print("we have arrived at location 3")
        break
    else: time.sleep(1)
    #==========================================================================================    
wp4_lat,wp4_lon=location_getter(wp3_lat,wp3_lon,0,-20)
wp4=LocationGlobalRelative(wp4_lat,wp4_lon,10)
vehicle.simple_goto(wp4)
while True:
    current_location=vehicle.location.global_relative_frame
    dist=distance_meters(current_location,wp4)
    print(f"the current distance from the target location {wp4} is {dist} meters")
    if dist<=1:
        print("we have arrived at location 4")
        break
    else: time.sleep(1)    
    #===========================================================================================================
#step6 we are going back to RTL
vehicle.mode=VehicleMode("RTL")
while vehicle.armed:
    a=vehicle.location.global_relative_frame.alt
    print(f"descending right now systems current altitude is {a} meters ")
    time.sleep(2)
print("We have landed successfully !")
vehicle.close()        