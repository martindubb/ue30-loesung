# zahlenvergleich 

z1 = 12
z2 = 8
z3 = 20

kleinste = {}
groesste = {}

# groesste
if z1 > z2:
    if z1 > z3:
        groesste = z1
    else:
        groesste = z3
else:
    if z2 > z3:
        groesste = z2
    else: 
        groesste = z3

# kleinste
if z1 < z2:
    if z1 < z3:
        kleinste = z1
    else:
        kleinste = z3
else:
    if z2 < z3:
        kleinste = z2
    else: 
        kleinste = z3


print("alle zahlen:", z1, z2, z3)
print("kleinste zahl:", kleinste)
print("groesste zahl:", groesste)