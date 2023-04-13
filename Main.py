def calculate_normal_force(weight, height, wheelbase, front_axle_dist, rear_axle_dist):
    fn = (weight / 2) + (front_axle_dist * height / wheelbase) - (rear_axle_dist * height / wheelbase)
    return fn


def calculate_water_weight(density, gravity, depth, area):
    wl = density * gravity * depth * area
    return wl


def calculate_coefficient_of_friction(force, weight, downforce, drag, water_weight):
    mu = (force / weight) + (downforce / weight) + (drag / weight) - (water_weight / weight)
    return mu


def calculate_threshold_of_traction(mu, fn):
    f_max = mu * fn
    return f_max

# Constants
GRAVITY = 9.81
DENSITY = 1000

# Sample values
mass = 1000
height = 0.5
wheelbase = 2.5
front_axle_dist = 1.25
rear_axle_dist = 1.25
force = 10000
downforce = 1000
drag = 100
depth = 0.0
area = 0.1

# Calculate normal force (Fn)
normal_force = calculate_normal_force(mass, height, wheelbase, front_axle_dist, rear_axle_dist)

# Calculate water weight (Wl)
water_weight = calculate_water_weight(DENSITY, GRAVITY, depth, area)

# Calculate the coefficient of friction (µ)
coefficient_of_friction = calculate_coefficient_of_friction(force, mass, downforce, drag, water_weight)

# Calculate the threshold of traction (F_max)
threshold_of_traction = calculate_threshold_of_traction(coefficient_of_friction, normal_force)

print("Threshold of Traction (F_max):", threshold_of_traction)
print(f"In meters per second that is", threshold_of_traction / mass)

