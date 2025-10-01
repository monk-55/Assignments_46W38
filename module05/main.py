"""
This function calculates the power output of a wind turbine based on a given wind speed (wind_speed) and the following default parameters:

rated power (rated_power), with a default value: 15,
cut-in wind speed (cut_in), with a default value: 3,
rated wind speed (rated_wind_speed), with a default value: 11,
cut-out wind speed (cut_out), with a default value: 25
Also an interpolation option is required in the inputs(int_option), a string to define the interpolation method, This can only be "linear" or "cubic"and has
a default value: "linear".

If the user wants to leave all defaults as they are then only the wind_speed needs to be specified, otherwise please specify the values required for
any of the other inputs. As above when specifying int_option only enter 'linear' or 'cubic'.

Module05 - Modified code to use a numpy array as input
"""

#Function definition including default values for everything except wind_speed. Note int_option is a string
import numpy as np
import time as time

# def calculate_power_output(wind_speed, rated_power = 15, cut_in = 3, rated_wind_speed = 11, cut_out = 25, int_option = 'linear'):
#     """
#     The following code checks the interpolation method and then uses np where to apply conditions when this is used
#     """
#     if int_option == 'linear':
#         calc_power = rated_power*((wind_speed - cut_in) / (rated_wind_speed - cut_in))
#     elif int_option == 'cubic':
#         calc_power = rated_power*((wind_speed**3)/(rated_wind_speed**3))
#     else: 
#         raise ValueError(f"{int_option} is not a valid option, please specify linear or cubic")
        
     
    
#     power = np.where((wind_speed < cut_in) | (wind_speed>= cut_out), 0, \
#                      np.where((wind_speed>=rated_wind_speed) & (wind_speed<cut_out),  rated_power, calc_power))
        
#     return power


#alternative using masks
def calculate_power_output(wind_speed, rated_power = 15, cut_in = 3, rated_wind_speed = 11, cut_out = 25, int_option = 'linear'):
    """
    The masks identify which values in the array need to have power calculated or are at rated power
    An empty array (power) is created at the beginning that is full of zeros and set to the same
    shape as the wind speed array. Therefore where the wind speed is not within operational range then the
    power is already at 0 by default and no operation is required
    """
    power = np.zeros(wind_speed.shape)
    mask_rated = (wind_speed >= rated_wind_speed) & (wind_speed < cut_out)
    mask_power_output = (wind_speed>=cut_in) & (wind_speed < rated_wind_speed)

    if int_option == 'linear':
        power[mask_power_output] = rated_power*((wind_speed[mask_power_output] - cut_in) / (rated_wind_speed - cut_in))
    elif int_option == 'cubic':
        power[mask_power_output] = rated_power*((wind_speed[mask_power_output]**3)/(rated_wind_speed**3))
    else: 
        raise ValueError(f"{int_option} is not a valid option, please specify linear or cubic")
        
    power[mask_rated] = rated_power 
    
        
    return power


if __name__ == '__main__':
    # Example 
   # wind_speed = np.array([[2.1,8.4,5.2,11.6],[25.0,27.1,13.6,3.2]])
    rng = np.random.default_rng()
    wind_speed =  np.round(rng.random((30,5))*30,2)
    power = np.round(calculate_power_output(wind_speed),2)
    print(f'wind speeds = {wind_speed}, power = {power}') 
    np.savetxt('output_windspeeds.txt', wind_speed,fmt ="%.2f")
    np.savetxt('output_powers.txt', power, fmt="%.2f")


    print(time.time())






