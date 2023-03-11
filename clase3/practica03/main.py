import sqlite3
from alumno import alumno
from colegio import colegio
from dao import dao

con = None

try:
    """connection to interact with the databasse"""
    con = sqlite3.connect('./mydatabase.db')

    """Table creation both students and school"""
    dao.crear_tabla_alumno(con)
    dao.crear_tabla_colegio(con)

    """Instantiating student and school"""
    alum1 = alumno("Pedro", "xxx")
    alum2 = alumno("Sara", "zzz")

    col1 = colegio("Juan", "aaa", "Gómez", "Dos Parques")
    col2 = colegio("Enma", "bbb", "Fernandez", "Joaquin Costa")

    """Insert into the table an student and school"""
    dao.insertar_registro(con, alum1, "alumno")
    dao.insertar_registro(con, alum2, "alumno")

    dao.insertar_registro(con, col1, "colegio")
    dao.insertar_registro(con, col2, "colegio")

    """Recover all the data"""
    dao.recuperar_datos(con, "alumno")
    dao.recuperar_datos(con, "colegio")

    """Delete the table"""
    dao.borrar_tabla(con, "alumno")
    dao.borrar_tabla(con, "colegio")

except Exception as e:
    print("Error en el main: ",e)