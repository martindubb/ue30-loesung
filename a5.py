# schaltjahr

jahr = int(input("jahr: "))
is_schaltjahr = False

if jahr % 4 == 0: # durch 4 teilbar
    if jahr % 100 != 0: # nicht durch 100 teilbar
        is_schaltjahr = True
    elif jahr % 400 == 0: # aber durch 400 teilbar
        is_schaltjahr = True


if is_schaltjahr:
    print(jahr, "war ein Schaltjahr!")
else:
    print(jahr, "war KEIN Schaltjahr!")
    