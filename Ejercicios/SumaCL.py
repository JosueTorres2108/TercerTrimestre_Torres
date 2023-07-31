def SumaL(file):
    contador = 0
    read_txt = open(file,"r")
    for i in read_txt.readlines():
        contador += 1
    if contador == 1:
        print("El archivo tiene ", contador,"linea")
    elif contador > 1:
        print("El archivo tiene ", contador,"lineas")
    else: 
        print("No tiene lineas")
    read_txt.close
    
def SumaC(file):
    contador = 0
    read_txt = open(file,"r")
    for i in read_txt.read():
        contador += 1
    if contador == 1:
        print("El archivo tiene ", contador,"caracter")
    elif contador > 1:
        print("El archivo tiene ", contador,"caracteres")
    else: 
        print("No tiene caracteres")
    read_txt.close
    
SumaL ("nuevo.txt")
SumaC ("nuevo.txt")