class alumno:
    """
    Alumno class mainly contains information about a person.

    Parameters  
    ----------
    nombre: str 
        This variable stores the person's name.
    dni: str
        A unique number being used as a key in the database. 

    Attributes
    ----------
    nombre: str
        This is where we stored nombre
    dni: str
        This is where we stored dni

    """
    def __init__(self,nombre, dni):
        self.__nombre = nombre
        self.__dni = dni

    def setNombre(self, nombre):
        """Setter method.

        Parameters: 
        nombre (str): The name of a person.

        Instance variable:
        To change the value.

        """
        self.__nombre = nombre
    
    def getNombre(self):
        """Getter method.

        Returns (str): Returning the name.
        
        """
        return self.__nombre
    
    def setDNI(self, dni):
        """Setter method.

        Parameters: 
        nombre (str): The id of a person.

        Instance variable:
        To change the value.

        """
        self.__dni = dni
    
    def getDNI(self):
        """Getter method.

        Returns (str): Returning the id.
        
        """
        return self.__dni
    