# 1. importacion de librerias

# 2. constantes MAYUSCULAS

# 3. clase
class Operaciones:
    """
    docstring
    """
    def __init__(self, num1, num2):
        # atributos de clase
        self.num1 = num1
        self.num2 = num2

    # funcionalidades
    def sumar(self):
        """
        docstring
        """
        return self.num1 + self.num2
    
    def restar(self):
        """
        docstring
        """
        return self.num1 - self.num2

    def multiplicar(self):
        """
        docstring
        """
        return self.num1 * self.num2
    
    def dividir(self):
        """
        docstring
        """
        return self.num1 / self.num2

    def potenciacion(self, exponente=2):
        """
        docstring
        """
        return self.num1 ** exponente


# 4. Programa principal
if __name__ == "__main__":    
    # ingreso de datos
    num1 = float(input('Ingrese el primer número: '))
    num2 = float(input('Ingrese el segundo número: '))

    # Instanciando clase (creas el objeto)
    oper = Operaciones(num1, num2)


    # Realizando la operacion de suma
    print(f'La suma de los numero es {oper.sumar()}')

    # Potenciacion
    exponente = int(input('Ingrese el exponente: '))
    p = oper.potenciacion(exponente)

    print(f'el numero {oper.num1}, elevado a la {exponente}, es : {p}')

    pass # pass no realiza ninguna accion


