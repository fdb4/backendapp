import mysql.connector
import os
base_dir=os.path.dirname(os.path.realpath(__file__))
class dbcon:#creates connection to database
    def __init__(self):
        self.config={
        'user': '',#settheselater
        'password': '',
        'host': 'mysql1070.mysql.database.azure.com',
        'database': 'schema',
        'ssl_ca':base_dir+r'\DigiCertGlobalRootCA.crt.pem',
        }
    def print(self):
        print(self.config)
    def ctdb(self): #connect to database
        self.con=mysql.connector.connect(**self.config)

    def closecon(self):
        self.con.close()

