import sqlite3
from alumno import alumno
from colegio import colegio

class dao:
    """
    The dao class has been created in order to interact which the database to add, query
    and delete the information from alumno. 
    """

    def crear_tabla_alumno(con):
        """This method is meant to be created the student table in case it does not exist.
        
        Parameters: 
        con: The needed connection to be capable of database interaction.
        """
        try:
            sql = '''
                create table if not exists alumnos(
                    nombre varchar (100),
                    dni varchar (10) primary key
                )
                '''
            cursor = con.cursor()
            cursor.execute(sql)
            print("La tabla se ha creado correctamente")
        except Exception as e:
            print("Error al crear la tabla alumno: ",e)
    
    def crear_tabla_colegio(con):
        """This method is meant to be created the school table in case it does not exist.
        
        Parameters: 
        con: The needed connection to be capable of database interaction.
        """

        try:
            sql = '''
                create table if not exists colegios(
                    nombre varchar (100),
                    apellido varchar(100),
                    dni varchar (10) primary key,
                    colegio varchar(100)
                )
                '''
            cursor = con.cursor()
            cursor.execute(sql)
            print("La tabla se ha creado correctamente")
        except Exception as e:
            print("Error al crear la tabla colegio: ",e)

    def insertar_registro(con, object, cadena_texto):
        """This method is meant to be added a new entrance to the table.
        
        Parameters: 
        con: The needed connection to be capable of database interaction.
        object: Here we shared the personal information that is stored in the database. 
                The object contains the name and id. 
        cadena_texto: This variable identifies whether it is a student or a school to be performed different actions.
        """
        try:
            if cadena_texto == "alumno":
                sql = '''
                    insert into alumnos(nombre, dni)
                    values (?,?)
                '''
                parametro = (object.getNombre(), object.getDNI())

            if cadena_texto == "colegio":
                sql = '''
                    insert into colegios(nombre, dni, apellido, colegio)
                    values (?,?,?,?)
                '''
                parametro = (object.getNombre(), object.getDNI(), object.getApellidos(), object.getColegio())

            cursor = con.cursor()
            cursor.execute(sql,parametro)
            con.commit()
            print("El registro se ha insertado")
        except Exception as e:
            print("Error al insertar registros : ",e)

    def recuperar_datos(con, cadena_texto):
        """This method is meant to be recoved the information either from student or school
        
        Parameters: 
        con: The needed connection to be capable of database interaction.
        cadena_texto: This variable identifies whether it is a student or a school to be performed different actions.
        """ 
        try:
            if cadena_texto == "alumno":
                sql = '''
                    select * from alumnos            
                '''

            if cadena_texto == "colegio":
                sql = '''
                    select * from colegios            
                '''

            cursor = con.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            print(rows)
        except Exception as e:
            print("Error al recuperar los datos: ", e)
    
    def borrar_tabla(con, cadena_texto):
        """This method is meant to be removed the table student or school
        
        Parameters: 
        con: The needed connection to be capable of database interaction.
        cadena_texto: This variable identifies whether it is a student or a school to be performed different actions.
        """ 
        try:
            if cadena_texto == "alumno":
                sql = '''
                    delete from alumnos            
                '''

            if cadena_texto == "colegio":
                sql = '''
                    delete from colegios            
                '''
            
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()
            print("La tabla esta vacia")
        except Exception as e:
            print("Error: ", e)

    