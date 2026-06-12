#Altitude and air density calculator
#international standard atmosphere(ISA)model
def air_density(altitude):
    #Sea level values
    rho_o=1.225 #kg/m^3
    Height=8500 #scale height in metres
    density=rho_o*(2.718**(-altitude/Height))
    return density
def speed_of_sound(altitude):
    #temperature decreases with increase in altitude in troposphere
    Ta=288.5 #sea level temperature in kelvin 
    L=0.0065 #lapse rate
    T=Ta-L*altitude
    gamma=1.4
    R=287 #J/Kg/K
    a=(gamma*R*T)**0.5
    return a
# Let's test the functions at an altitude of 1000 meters
test_altitude = 2000

# Call the functions and store the results
current_density = air_density(test_altitude)
current_speed = speed_of_sound(test_altitude)

# Print the results to the terminal
print("Air Density:", current_density)
print("Speed of Sound:", current_speed)