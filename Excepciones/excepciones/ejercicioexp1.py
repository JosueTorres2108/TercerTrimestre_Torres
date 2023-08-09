### Assert ###

def Cuadratica_assert ():
    try:
        a = float(input("Digita un numero para el valor A: "))
        b = float(input("Digita un numero para el valor B: "))
        c = float(input("Digita un numero para el valor C: "))

        x = b**2 - (4*a*c)
        
        assert x>0
        
        raiz = x**0.5

        sustraccion = -b -raiz
        adicion = -b + raiz

        assert not(a == 0)
        
        divi_sus = sustraccion/(2*a)
        divi_adi = adicion/(2*a)


        print(f"La ecuacion cuadratica de la suma es: {divi_adi}")
        print(f"La ecuacion cuadratica de la resta es: {divi_sus}")

    except AssertionError:
        print("ohh... ah ocurrido un error!. Buscalo!")
    except ValueError:
        print("No se puede ingresar tipos de datos que no sean enteros o flotantes")
    except KeyboardInterrupt:
        print("Se ha interrumpido el proceso del programa")

Cuadratica_assert ()

### Raise ####

def Cuadratica_raise ():
    try:
        a = float(input("Digita un numero para el valor A: "))
        b = float(input("Digita un numero para el valor B: "))
        c = float(input("Digita un numero para el valor C: "))
        
        x = b**2 - (4*a*c)
        
        if not(x>0):
            raise TypeError
        
        raiz = x**0.5

        sustraccion = -b -raiz
        adicion = -b + raiz

        if a==0:
            raise ZeroDivisionError
        
        divi_sus = sustraccion/(2*a)
        divi_adi = adicion/(2*a)


        print(f"La ecuacion cuadratica de la suma es: {divi_adi}")
        print(f"La ecuacion cuadratica de la resta es: {divi_sus}")

    except ZeroDivisionError:
        print("No se puede dividir los valores entre 0")
    except ValueError:
        print("No se puede ingresar tipos de datos que no sean enteros o flotantes")
    except TypeError:
        print("No se puede sacar raiz de numero negativos")
    except KeyboardInterrupt:
        print("Se ha interrumpido el proceso del programa")
    except:
        print("ohh... ah ocurrido un error!. Buscalo!")

Cuadratica_raise ()