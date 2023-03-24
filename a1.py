def swap(ch):
    # NEU: mit python-mitteln
    if ch.isupper():
        return ch.lower()
    else:
        return ch.upper()
    # ALT: mit ASCII-Zahlen
    # c = ord(ch)
    # if (c >= 65) and (c <= 90):
    #     c += 32
    # elif c >= 97 and c <= 122:
    #     c -= 32
    # return chr(c)


file = input("Textdatei angeben: ")
with open(file, "r") as f:
    while True:
        line = f.readline()
        if line == "":
            break
        for i in range(len(line)):
            print(swap(line[i]), end="")
    print()