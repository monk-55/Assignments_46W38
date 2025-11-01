import numpy as np
import pandas as pd

class GeneralWindTurbine(object):
    def __init__(self, rotor_diameter, hub_height, rated_power, v_in, v_rated, v_out, name = None):
        self.rotor_diameter = rotor_diameter  # m
        self.hub_height = hub_height    # m
        self.rated_power = rated_power
        self.v_in = v_in
        self.v_rated = v_rated
        self.v_out = v_out
        self.name = name


    def get_power(v):
        if v< v_in | v > v_out:
            P = 0
        elif vrated <= v < v_out:
            P = rated_power
        else:
            P = rated_power*((v/v_rated)**3)
        
        return P

class WindTurbine(GeneralWindTurbine):
    def __init__(self, rotor_diameter, hub_height, rated_power, v_in, v_rated, v_out, power_curve, name=None):
        super().__init__(rotor_diameter, hub_height, rated_power, v_in, v_rated, v_out, name)
        self.power_curve = power_curve





if __name__ == '__main__':
    turbine = GeneralWindTurbine