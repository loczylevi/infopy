
import math
a = int(input(""))
b = int(input(""))
c = int(input(""))

diszkriminans = (b**2-4*a*c)

if diszkriminans > 0:
    minusz = (-b - math.sqrt(diszkriminans))/ (2*a)
    plusz = (-b + math.sqrt(diszkriminans))/(2*a)
    print(f"két valós gyök van\n{minusz}\n{plusz}")

elif diszkriminans == 0:
    print(-b / (2*a))
else:
    print("komplex szám")


