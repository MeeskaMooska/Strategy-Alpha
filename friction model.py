def calculate_fn(weight, height, wheelbase, front_axle_dist, rear_axle_dist):
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


# Sample values
mass = 1000
height = 0.5
wheelbase = 2.5
front_axle_dist = 1.25
rear_axle_dist = 1.25
force = 10000
downforce = 1000
drag = 100
density = 1000
gravity = 9.81
depth = 0.0
area = 0.1

# Calculate normal force (Fn)
fn = calculate_fn(mass, height, wheelbase, front_axle_dist, rear_axle_dist)

# Calculate water weight (Wl)
wl = calculate_water_weight(density, gravity, depth, area)

# Calculate the coefficient of friction (µ)
mu = calculate_coefficient_of_friction(force, mass, downforce, drag, wl)

# Calculate the threshold of traction (F_max)
f_max = calculate_threshold_of_traction(mu, fn)

print("Threshold of Traction (F_max):", f_max)
print(f"In meters per second that is", f_max / mass)
bore = 4.13
stroke = 3.984
displacement = (3.141/4) * (bore * bore) * stroke * 8
print((displacement * 5400 * 8) / 3456)
