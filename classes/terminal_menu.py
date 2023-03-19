import time, os

def main_menu():
    '''Hauptmenü'''
    print("Was möchten Sie tun?")
    print(f"(1) Eine Person suchen")
    print(f"(2) Ein Land suchen")
    print(f"(3) Eine Sprache suchen")
    print(f"(4) Daten löschen")
    print(f"(5) Das Programm beenden")

    eingabe = int(input(">> "))

    if eingabe == 5:
        print("Das Programm wird beendet.")
        time.sleep(1)
        os._exit(0)
    
    return eingabe

def personen_menu():
    print("(1) Suche über Vornamen")
    print("(2) Suche über ID")
    print("(3) Suche über Nachnamen")
    print("(4) Zurück zum Hauptmenü")
    print("(5) Programm beenden")

    eingabe = int(input(">> "))

    if eingabe == 5:
        print("Das Programm wird beendet.")
        time.sleep(1)
        os._exit(0)
    elif eingabe == 4:
        main_menu()
    return eingabe

def vornamen_menu():
    vorname = str(input("Vorname: >> "))
    return vorname
def id_menu():
    id = int(input("ID: >> "))
    return id

def name_menu():
    name = str(input("Name: >> "))
    return name

def delete_menu():
    print(f"(1) Alle Daten einer Tabelle löschen.")
    print(f"Geben Sie den Tabellennamen ein (laender, personen oder sprachen)")
    eingabe = str(input(">>: "))
    return eingabe



if __name__=="__main__":
    main_menu()