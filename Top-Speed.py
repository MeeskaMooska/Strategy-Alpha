import math

def calculate_top_speed(engine_power, drag_coefficient, frontal_area, air_density, rolling_resistance_coefficient, weight):
    numerator = 2 * engine_power
    denominator = (drag_coefficient * frontal_area * air_density) + (2 * rolling_resistance_coefficient * weight)
    top_speed = (2 * engine_power / (air_density * frontal_area * drag_coefficient)) ** (1/3)
    return top_speed

# F1 car values
f1_engine_power = 7350000  # Watts (equivalent to 1000 hp)
f1_drag_coefficient = .7
air_density = 1.225  # kg/m^3 (at sea level and 15°C)
f1_frontal_area = 1.6  # square meters
f1_rolling_resistance_coefficient = 0.008
f1_weight = 752  # kg

# Calculate top speed (m/s)
f1_top_speed_mps = calculate_top_speed(f1_engine_power, f1_drag_coefficient, f1_frontal_area, air_density, f1_rolling_resistance_coefficient, f1_weight)
print(f"F1 car top speed: {f1_top_speed_mps:.4f} m/s")

# Convert top speed to km/h
f1_top_speed_kph = f1_top_speed_mps * 3.6
print(f"F1 car top speed: {f1_top_speed_kph:.4f} km/h")

# Convert top speed to mph
f1_top_speed_mph = f1_top_speed_mps * 2.237
print(f"F1 car top speed: {f1_top_speed_mph:.4f} mph")




# Constants
P = 735000  # Engine power in watts
Cd = 0.7  # Drag coefficient of the car
A = 1.5  # Frontal area of the car in square meters
rho = 1.225  # Air density in kilograms per cubic meter

# Calculate maximum speed
V = math.pow((2 * P / (rho * Cd * A)), 1/3)

print("The maximum speed of the car is:", round(V * 2.237, 4), "miles per hour.")