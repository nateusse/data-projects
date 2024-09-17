import pandas as pd # type: ignore
import sqlite3 as sql

datos = pd.read_csv('../data/poblacion.csv')
#print(datos.head(10)) #10 priemras filas
#print(datos.tail(10))  #10 ultimas filas
#print(datos.info())  #informacion de las columnas (nombre, tipo, cantidad de datos)
#print(datos.describe()) #estadisticas basicas de las columnas numericas
#  (count, mean, std, min, 25%, 50%, 75%, max)
#print(datos.shape) #tupla, no metodo, (72, 8)
#print(datos.dropna(axis=1)) #borra columnas con valores nulos
#print(datos.drop_duplicates()) #borra filas duplicadas
datos.rename(columns = {'Y':"Year", "Estados Unidos":"USA"}) #cambia el nombre de la columna Y por Year
#print(datos.drop(columns = ['Nigeria',"Pakistan"])) #borra las columna Y
#(datos.drop(columns ="Nigeria", inplace = True)) #borra la columna Nigeria


# SQL 
conexion = sql.connect('../data/poblacion.db')
conexion.commit() #guarda/confirma los cambios, revierte es rrollback(), cerrar .close()
cursor = conexion.cursor() #crear un cursor, para ejecutar comandos
conexion.execute("""
CREATE TABLE IF NOT EXISTS habitantes(
    Years INT, 
    USA REAL, 
    India REAL, 
    China REAL, 
    Indonesia REAL, 
    Pakistan REAL, 
    Brasil REAL, 
)
""")  #""" para escribir en varias lineas, no solo por executescript
conexion.commit()
cursor.execute("INSERT INTO habitantes VALUES(1910, 448.77, 253.1, 117.1, 78.86, 27.46, 43.15)")
conexion.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS prueba(
    Nombre TEXT,
    Edad INT,
    Pais TEXT
)
""") 
cursor.execute("INSERT INTO prueba VALUES('Juan', 25, 'Peru')")
conexion.commit()