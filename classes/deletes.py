from .connector import *
import os

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
    
    



