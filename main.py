from classes import queryClass,insertClass,deleteClass, sleep_timer
from classes import  terminal_menu as menu
import os


def main():
    print("******************************************")
    print("*\t Das Personenverwaltungssystem \t *")
    print("******************************************\n\n")
    sleep_timer()
    eingabe = menu.main_menu()
    #print(eingabe)

    if eingabe ==1:
        personenSuche = menu.personen_menu()
        if personenSuche == 1:
            eingabe = menu.vornamen_menu()
            Abfrage = queryClass()
            Abfrage.sucheVorname(eingabe)
        if personenSuche == 2:
            eingabe = menu.id_menu()
            Abfrage = queryClass()
            Abfrage.sucheID(eingabe)
        if personenSuche == 3:
            eingabe = menu.name_menu()
            Abfrage = queryClass()
            Abfrage.sucheName(eingabe)
    if eingabe == 4:
        data_delete = menu.delete_menu()
        data_deleted = deleteClass()
        data_deleted.deleteAll(data_delete)




if __name__=="__main__":
    
    main()