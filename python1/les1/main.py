def get_dims():
    x = float(input("breedte: "))
    z = float(input("lengte: "))
    y = float(input("hoogte: "))
    return (x,y,z)

def calc_m3(x, y, z):
    return x * y * z

def calc_m2(z1, z2):
    return z1 * z2

def calc_plank_m2(x, y, z):
    m2_top = calc_m2(x, z)
    m2_front = calc_m2(x, y)
    m2_side = calc_m2(y, z)
    total_m2 = (2*m2_top) + (2*m2_front) + (2*m2_side)
    return total_m2

def calc_m2_costs(m2):
    prijs_m2 = 15
    return prijs_m2 * m2

(x, y, z) = get_dims()
m3 = calc_m3(x, y, z)
total_m2 = calc_plank_m2(x, y, z)
print(f"De kist heeft een inhoud van {m3} m3 en heeft {total_m2} m2 aan panelen nodig")
print(f"De kist kost {calc_m2_costs(total_m2)} euro om te maken")