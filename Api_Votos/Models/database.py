import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1025887569",
        database="Votos_bd"
    )
    return connection
