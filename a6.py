# wasnt me

eingabe = input("Funktioniert das System? [J/N]")
if eingabe.upper() == "J":
    print("nicht rumfummeln")
    print("alles gut")
else:
    eingabe = input("Bist du schuld? [J/N]")
    if eingabe.upper() != "J":
        print("dich trifft es nicht")
    else:
        print("idiot")
        eingabe = input("Jemand bemerkt? [J/N]")
        if eingabe.upper() != "J":
            print("man wird dich nicht finden")
        else:
            print("am arsch")
            eingabe = input("unterejubeln möglich? [J/N]")
            if eingabe.upper() == "J":
                print("am arsch - aber jemand anderes")
            else:
                print("am arsch - ABER WIRLICH")