import datetime, time

# Das Ziel-Datum
ziel_datum = datetime.datetime(2023, 4, 11)

while True:
    # Aktuelles Datum und Uhrzeit
    jetzt = datetime.datetime.now()

    # Unterschied zwischen dem Ziel-Datum und der aktuellen Zeit
    diff = ziel_datum - jetzt

    # Wenn das Ziel-Datum erreicht wurde, beenden wir den Countdown
    if diff.total_seconds() < 0:
        print("Endlich Osterferien!!!")
        break

    # Ausgabe des Countdowns
    tage = diff.days
    stunden, rest = divmod(diff.seconds, 3600)
    minuten, sekunden = divmod(rest, 60)
    print(f"Noch {tage} Tage, {stunden} Stunden, {minuten} Minuten, {sekunden} Sekunden bis zum 11.04.2023")

    # Pause für eine Sekunde, bevor der Countdown aktualisiert wird
    time.sleep(1)
