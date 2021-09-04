


class Alumno:
    def __init__(self, nombre, registro):
        """
        Todo alumno debe tener un nombre y nro de registro
        """
        self.nombre = nombre
        self.nro_registro = registro

    
    def display(self):
        """
        Metodo que muestra la informacion del estudiante
        """
        print('Estudiante de nombre {} y con nro de registro {}'.format(self.nombre ,self.nro_registro))
    
    def setAge(self, edad):
        """
        Agrega un atributo age a mi clase Alumno
        """
        self.age = edad
        print('mi alumno {} tiene {} años'.format(self.nombre, self.age))
    
    def setNota(self, nota_curso):
        self.nota = nota_curso
        print('mi alumno {} tiene {} en el curso de historia'.format(self.nombre, self.nota))


    pass

if __name__=='__main__':
    
    # creando objetos
    alumno1 = Alumno('Gonzalo','XP567')

    alumno2 = Alumno('Cesar','XP987')

    alumnos = []
    for i in range(4):
        nombre = input(f'Ingrese el nombre del alumno {i + 1}')
        registro = input(f'Ingrese su nro de registro: ')

        alumnos.append(Alumno(nombre,registro))
    
    
    # alumnos = [Alumno('Gonzalo', 'XP567'), Alumno('Juan','XP562'), Alumno('Maria','XP652')]
    
    # obteniendo el nombre de mi objeto alumno2
    #print(f'EL nombre de mi alumn2 es: {alumno2.nombre}')

    # # llamando al metodo display
    # alumno1.display()

    # alumno2.display()

    # # llamando metodo set age
    # alumno1.setAge(18)

    # # llamando metodo setNota
    # alumno2.setNota(18)

    for alum in alumnos:
        alum.display()
    
    pass
