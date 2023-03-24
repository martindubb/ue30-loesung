# Aufgabe 1

## a) Erkläre was der Algorithmus tut. 
Der Algorithmus liest Text aus einer Datei ein und tauscht Groß- in Kleinbuchstaben und Klein- in Großbuchstaben. 
Die einzelnen Buchstaben werden der Funktion "swap" übergeben. 
Das Ergennis aus der Funktion "swap" wird dann nach stdout gedruckt.

## a) Was passiert in der Funktion swap()?
Dort wird zunächst der Zahlenwert des ASCII-Zeichens ermittelt. Dieser Zahlenwert wird angepasst, je nachdem ob es sich um Groß- oder Kleinbuchstaben handelt. Ist der Wert angepasst wird es wieder in ein Zeichen umgewandelt und zurückgegeben. 

## c) Kann die Funktion swap()mit Python-Mittel vereinfacht werden? Wenn ja, wie?
Ja, siehe 'a1.py':
```
def swap(ch):
    # NEU: mit python-mitteln
    if ch.isupper():
        return ch.lower()
    else:
        return ch.upper()
```

