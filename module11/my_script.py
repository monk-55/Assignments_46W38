import math, sys


def Calculate_Power(windspeed, rotor_diameter, air_density=1.225):
    if windspeed < 0:
        return 0
    area = math.pi * (rotor_diameter / 2) ** 2
    power = 0.5 * air_density * area * (windspeed**3)
    return power


def check_turbine_status(wind_speed, cut_in=3, cut_out=25):
    if wind_speed < cut_in:
        return "stopped"
    elif wind_speed > cut_out:
        return "braked"
    else:
        return "operating"


result = Calculate_Power(15.5, 120)
status = check_turbine_status(15.5)
print(f"Power output: {result} W, Status: {status}")
