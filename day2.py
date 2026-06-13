def speed_of_sound(altitude):
    #to make a function of speed of sound
    To=288.15 #sea level temperature in kelvin
    L=0.0065 #lapse rate
    T=To-L*altitude
    a=(1.4*287*T)**0.5
    return a
def Mach_number(velocity, altitude):
    #to make a function of Mach number
    a=speed_of_sound(altitude)
    M=velocity/a
    return M
def flow_regime(M):
    #to make a function of flow regime 
    if M<0.3:
        return "Incompressible"
    elif M>=0.3 and M<0.8:
        return  "Subsonic"
    elif M>=0.8 and M<1.2:
        return "Transonic"
    elif M>=1.2 and M<5:
        return "supersonic"
    else: return "hypersonic"
#real world vehicles
Vehicles=[ 
    ("Shahed 136",51,500),
    ("F450 hobby drone",15,100),
    ("Boeing 737",250,10000),
    ("Brahmos",930,15000),
    ("SR 71 Blackbird",1000,24000),
]
print(f"{'Vehicle':<22}{'Speed':<12}{'altitude':<10}{'Mach':<8}{'flow_regime'}")
print("-"*65)
for name,V,Alt in Vehicles:
    M=Mach_number (V,Alt) 
    regime=flow_regime(M)
    print(f"{name:<22} {V:<12} {Alt:<10} {M:<8.3f} {regime}")

    
