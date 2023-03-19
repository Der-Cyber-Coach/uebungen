from .connector import *


class queryClass(verbindung):
    def __init__(self) -> None:
        super().__init__()
    
    def sucheName(self, test):
        with self.connection as connection:
            with connection.cursor() as cursor:
                qry = f"SELECT Vorname, Nachname FROM `personen` WHERE Nachname =%s"
                cursor.execute(qry,test)
                result = cursor.fetchone()
                if result == None:
                    print(f"Die Person {test} ist nicht im System vorhanden.")
                else:
                    print(result)

    def sucheID(self, id):
        with self.connection as connection:
            with connection.cursor() as cursor:
                qry = f"SELECT Vorname, Nachname FROM `personen` WHERE `ID`=%s"
                cursor.execute(qry,int(id))
                result = cursor.fetchone()
                if result == None:
                    print(f"Die ID {id} ist nicht im System vorhanden.")
                else:
                    print(result)

    def sucheVorname(self, test):
            with self.connection as connection:
                with connection.cursor() as cursor:
                    qry = f"SELECT Vorname, Nachname FROM `personen` WHERE Vorname =%s"
                    cursor.execute(qry,test)
                    result = cursor.fetchone()
                    if result == None:
                        print(f"Die Person {test} ist nicht im System vorhanden.")
                    else:
                        print(result)   