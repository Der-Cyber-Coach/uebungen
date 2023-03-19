import pymysql
from .connector import *
import os
import time


# database insert models

class insertClass(verbindung):

    def __init__(self) -> None:
        super().__init__()
    
    def insertPerson(self,Nachname:str, Vorname:str, Sprache:int,Land:int):
        '''adds a person into the database'''
        
        with self.connection as connection:
            with connection.cursor() as cursor:
                insert = f"INSERT INTO `personen`(`Nachname`, `Vorname`, `LAND`, `SPRACHE`) VALUES ('{Nachname}','{Vorname}','{Land}','{Sprache}')"
                try:
                    cursor.execute(insert)
                    connection.commit()
                    time.sleep(1)
                    print(f" {Vorname}, {Nachname} hinzugefügt.")
                except:
                    print(f"Person wurde nicht hinzugefügt.")
                    print(f"Das Programm endet in 3...")
                    time.sleep(1)
                    print(f"2")
                    time.sleep(1)
                    print(f"1")
                    time.sleep(1)
                    print(f"Programmende")
                    os._exit(1)

    def insertSprache(self, Name:str):
        with self.connection as connection:
            with connection.cursor() as cursor:
                insert = f"INSERT INTO `sprachen`(`Name`) VALUES ('{Name}')"
                try:
                    cursor.execute(insert)
                    connection.commit()
                    time.sleep(1)
                    print(f" Die Sprache {Name} wurde hinzugefügt.")
                except:
                    print(f"Person wurde nicht hinzugefügt.")
                    print(f"Das Programm endet bald.")
                    time.sleep(2)
                    os._exit(1)


    def insertLand(self, Name:str):
            with self.connection as connection:
                with connection.cursor() as cursor:
                    insert = f"INSERT INTO `laender`(`Name`) VALUES ('{Name}')"
                    try:
                        cursor.execute(insert)
                        connection.commit()
                        time.sleep(1)
                        print(f"Das Land {Name} wurde hinzugefügt.")
                    except:
                        print(f"Person wurde nicht hinzugefügt.")
                        print(f"Das Programm endet bald.")
                        time.sleep(2)
                        os._exit(1)

                    

                    
        

if __name__=="__main__":

    test = insertClass()
    test.insertPerson('Mayer','Rudolf',1,6)


