G = 6.67430e-11  # gravitational constant
m1 = float(input("Enter mass of first object (kg): "))
m2 = float(input("Enter mass of second object (kg): "))
d = float(input("Enter distance between the objects (m): "))

force = G * (m1 * m2) / d**2
print(f"Gravitational force: {force} N")
