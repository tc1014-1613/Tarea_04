#encoding: UTF-8
# Autor: Marlon Brandon Velasco Pinello, A01379404
# Descripcion: paquetes Tarea 4 


#calcular el descuento
def calcularDescuento(paquetes):
    if paquetes==0:
        total=0
    elif paquetes > 0 and paquetes <=9:
        total=paquetes*1500
    elif paquetes >= 10 and paquetes <=19:
        total=(1500*paquetes)*0.8
    elif paquetes >= 20 and paquetes <=49:
        total=(1500*paquetes)*0.7
    elif paquetes >= 50 and paquetes <=99:
        total=(1500*paquetes)*0.6
    elif paquetes >= 100:
        total=(1500*paquetes)*0.5
    return total

#funcion principal main
def main():
    paquetes=int(input("Ingresa la cantidad de paquetes a comprar"))
    if paquetes < 0:
        print("Error: cantidad no valida")
    else:
        total=calcularDescuento(paquetes)
        print("el total a pagar es:",total)
        
main()
        