"""
No idea what I am doing here :)
Need to create a function that estimates pi
Thinking perhaps creating coordinates is the way to go as these will be 0 to 1 
along the x and y axis.
Then would need to calculate the distance from 0,0 for each one which might be tricky

"""
import numpy as np

def estimate_PI(num_points, seed=None):
    rng = np.random.default_rng()
    samples_x = rng.random(num_points, seed)
    samples_y = rng.random(num_points, seed)
    samples = np.column_stack((samples_x, samples_y))

    distances = np.sqrt(((samples[:,0]-0)**2)+((samples[:,1]-0)**2))

    lessthan1_mask = (distances < 1).astype(int)

    circle_count = lessthan1_mask.sum()

    pi_est = 4*(circle_count/num_points)



    return pi_est


print(estimate_PI(7000000))


