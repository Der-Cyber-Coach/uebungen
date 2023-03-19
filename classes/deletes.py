from .connector import *
from .terminal_menu import *
import os,time

class deleteClass(verbindung):
    def __init__(self) -> None:
        super().__init__()

    def deletePerson(self, Name:str, Vorname:str):
        with self.connection as connection:
            with connection.cursor() as cursor:
                delete = f"DELETE FROM `personen` WHERE `Nachname`='{Name}' AND `Vorname`='{Vorname}'"
                cursor.execute(delete)
                confirmation = int(input( f"ACHTUNG, SIE LÖSCHEN DATENSÄTZE! MÖCHTEN SIE DIE PERSON {Name}, {Vorname} wirklich löschen? \n 1 = JA, 2 = Nein \n >>"))

                if confirmation == 1:
                    connection.commit()
                    print(f"{Name}, {Vorname} wurde erfolgreich gelöscht")
                else:
                    print("ABBRUCH ERFOLGREICH")
                    os._exit(1)
    
    

    def deleteAll(self,tabelle:str):
        with self.connection as connection:
            with connection.cursor() as cursor:
                delete = f"DELETE FROM `{tabelle}`"
                print(f"Achtung, Sie löschen alle Datenbankinhalte.")
                print(f"Bitte bestätigen Sie das Löschen.")
                confirmation = str(input("Geben Sie OK ein: >>"))
                if confirmation == "OK":
                    try:
                        cursor.execute(delete)
                        connection.commit()
                        time.sleep(1)
                        print(f"Es wurden alle Daten aus der Tabelle {tabelle} gelöscht.")
                    except:
                        print("Löschen fehlgeschlagen. Zurück zum Hauptmenü...")
                        time.sleep(1)
                        main_menu()
                else:
                    print("Löschen abgebrochen. Zurück zum Hauptmenu...")
                    time.sleep(1)
                    main_menu()




