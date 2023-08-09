try:
    num=10
    for i in range(num):    
        if num%i==0:
            print(i,"es divisor")                
except:
    print('Error')
print('Este programa continua')



try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)
    lista=[1]
    print(lista[0.5])
    
except ValueError:
    print('Hubo un Error tipo VALUE')
except ZeroDivisionError:
    print('Hubo un Error tipo ZERO division')
except TypeError:
    print('Hubo un error indeterminado')
except:
    print('Otro error')

# t=(1,)
# t.append(10)

try:
    raise SyntaxError
except:
    print('Testing con raise y syntax error')
    
try:
    temperature = float(input('Ingresa la temperatura actual:'))

    if temperature > 0:
        print("Por encima de cero")
    elif temperature < 0:
        print("Por debajo de cero")
    else:
        print("Cero")
except NameError:
    print('name error')
    