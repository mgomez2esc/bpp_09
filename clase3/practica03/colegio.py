import alumno

class colegio(alumno.alumno):
    """
    Colegio contains information about a person which is sign up in the school.
    Colegio class inherits the functionality from alumno classs

    Parameters  
    ----------
    nombre: str 
        This variable stores the person's name. This variable is inherited from the alumno class.
    dni: str
        A unique number being used as a key in the database. This variable is inherited from the alumno class.
    apellidos: str
        This variable stores the person's surname.
    colegio: str
        It stores the colegio where the alumnos has been signed in.

    Attributes
    ----------
    nombre: str
        This is where we stored nombre
    dni: str
        This is where we stored dni
    apellidos: str
        It is where we stored the apellidos
    colegio: str
        It is where we stored the colegio

    """
    def __init__(self, nombre, dni, apellidos, colegio):
         super().__init__(nombre, dni)
         self.__apellidos = apellidos
         self.__colegio = colegio
    
    def setApellidos(self, apellidos):
        """Setter method.

        Parameters: 
        apellidos (str): The surname of a person.

        Instance variable:
        To change the value.

        """
        self.__apellidos = apellidos

    def getApellidos(self):
        """Getter method.

        Returns (str): Returning the surname.
        
        """
        return self.__apellidos

    def setColegio(self, colegio):
        """Setter method.

        Parameters: 
        apellidos (str): The school of a person.

        Instance variable:
        To change the value.

        """
        self.__colegio = colegio

    def getColegio(self):
        """Getter method.

        Returns (str): Returning the school.
        
        """        
        return self.__colegio
