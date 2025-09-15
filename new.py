

import math
print("Tartály festése")

m = int(input("Milyen magas?"))
d = float(input("Mennyi az átmérője?"))


t_fedel = (d/2)**2*math.pi

k_fedel = d * math.pi

t_palast = k_fedel * m

t_tartaly = 2 * t_fedel + t_palast

q = t_tartaly / 2

print(q)

px = int(input("Add meg a p pont x kordinátáját"))
py = int(input("Add meg a p pont x kordinátáját"))
qx = int(input("Add meg a p pont x kordinátáját"))
qy = int(input("Add meg a p pont x kordinátáját"))


dy = px - qx

dx = py - qy

l = (dx**2+dy**2)**0.5


print(f"P[{px},{py}] - Q[{qx},{qy}] => L: {l}")
