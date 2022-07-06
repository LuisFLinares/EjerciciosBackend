# crear una clase Persona en la cual se guarden su nombre, fecha_nacimiento, nacionalidad, dni, ademas tambien una clase Alumno y una clase Docente en la cual el alumno , a diferencia del docente, tenga una serie de cursos matriculados, y el docente por su parte tenga un numero del seguro social y su cuenta de la CTS. En base a lo visto de herencia crear las clases y ademas ver si hay algun atributo o metodo que deba de ser privado.


class Persona:
    def __init__(self, nombre, fecha_nacimiento, nacionalidad, dni):
        self.nombre = nombre 
        self.nacionalidad = nacionalidad
        self.dni = dni 
        self.fecha_nacimiento = fecha_nacimiento
        
    def info(self):
       
        data ={
                 "DNI":self.dni,
                "Fecha de nacimiento":self.fecha_nacimiento,
                "Nombre":self.nombre,
                "Nacionalidad":self.nacionalidad,
               }
        return data

class Alumno: 
    def __init__(self,cursos,nombre,fecha_nacimiento,nacionalidad,dni):
        self.nombre = nombre 
        self.nacionalidad = nacionalidad
        self.dni = dni 
        self.fecha_nacimiento = fecha_nacimiento
        self.cursos = cursos
    
    def info(self):
       
        data ={
                
                "Nombre":self.nombre,
                "Fecha de nacimiento":self.fecha_nacimiento,
                "Nacionalidad":self.nacionalidad,
                "DNI":self.dni,
                "Cursos":self.cursos,
               }
        return data

class Docente: 
    def __init__(self,nombre,fecha_nacimiento,nacionalidad,dni,cts,seguro_social):
        self.nombre = nombre 
        self.fecha_nacimiento = fecha_nacimiento
        self.dni = dni 
        self.nacionalidad = nacionalidad
        self.__numero_cts = cts 
        self.__seguro_social = seguro_social

    def info(self):
       
        data ={
                "Nombre":self.nombre,
                "Fecha de nacimiento":self.fecha_nacimiento,
                "Nacionalidad":self.nacionalidad,
                "DNI":self.dni,
                "CTS":self.__numero_cts,
                "SeguroSocial":self.__seguro_social,
               }
        
        return data
        

persona = Persona('Juan', '01/01/2000', 'Argentina', '12345678')
print(persona.info())

docente = Docente('Eduardo', '04/03/1900', 'Peruano', '5548775', '123456789', '7898955949')
print(docente.nombre)
print(docente.info( ))

alumno = Alumno('Luis', '021/02/1998', 'Peruano', '5548775', 'FullStack developer')
