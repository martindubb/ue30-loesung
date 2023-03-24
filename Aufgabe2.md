# Aufgabe 2

## Code1:
Zeile 4: 
`i += 1` erhöht i um 1
in Zeile 5 wird auf einen konreten index zugegriffen, der im letzten Schleifendurchgang bereits außerhalb der Range liegt. 
Lösung: erhöhe i NUR bei der Ausgabe: 
```
def print_list(list):
    l = len(list)
    for i in range(l):
        print(i+1, list[i])
```

## Code2:
Es soll in die Datei geschrieben werden, allerdings wird die Datei zum lesen geöffnet (Zeile 1)
Lösung: öffne Datei zum schreiben (und schließe sie wieder)
```
file = open("env", "w")
env_vars = "USER=otto\nPASS=otto\nHOST=192.168.0.34"
file.write(env_vars)
file.close()
```

## Code3:
Es sollten 12 Dateien erstellt werden. Fehler in Zeile 3: x wird erhöht, das wird aber nirgendwo gespeichert. 
Lösung: in Variable speichern!
```
x = 0
while x < 12:
    x = x + 1
    name = "datei"+str(x)+".txt"
    open(name, "a")
    print("datei", name, "erstellt")
```
