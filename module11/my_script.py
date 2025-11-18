"""Module to calculate power and check turbine status"""

import math


def calculate_power(windspeed, rotor_diameter, air_density=1.225):
    """Calculate power based on wind speed, RD and air density"""
    if windspeed < 0:
        return 0
    area = math.pi * (rotor_diameter / 2) ** 2
    power = 0.5 * air_density * area * (windspeed**3)
    return power


def check_turbine_status(wind_speed, cut_in=3, cut_out=25):
    """Return turbine status from input wind speed"""
    if wind_speed < cut_in:
        return "stopped"
    if wind_speed > cut_out:
        return "braked"
    return "operating"


result = calculate_power(15.5, 120)
STATUS = check_turbine_status(15.5)
print(f"Power output: {result} W, Status: {STATUS}")
