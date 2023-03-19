import pymysql

class verbindung:
    def __init__(self) -> None:
        try:
            self.connection = pymysql.connect(host='127.0.0.1', user='root',password='',database='uebung', cursorclass=pymysql.cursors.DictCursor)
            print('Verbindung hergestellt')
        except:
            print('Keine Verbindung')


    






if __name__=='__main__':
   pass