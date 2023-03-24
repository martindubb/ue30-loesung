# suchen in liste

def suche(liste, elem):
    for entry in liste:
        if entry == elem:
            return True
    return False

def myprint(result, word):
    if result == True:
        print("Ja, die Liste enthält", word)
    else:
        print("Nein", word, "ist nicht vorhanden")


mylist = ["Huhn", "Kuh", "Pferd", "Katze", "Hund", "Maus"]
word = "Schaaf"
result = suche(mylist, word)
myprint(result, word)

word = "Hund"
result = suche(mylist, word)
myprint(result, word)
