#encoding: UTF-8
#Autor: Jess Perea
#Nmeros Romanos        

#empieza 

from Graphics import*  #importar librerias

def calcularArea1(ancho1,alto1):  #calcula el area del primer triangulo
    area1 = (ancho1 * alto1)
    return area1 
    
def calcularArea2(ancho2,alto2): #calcula el area del triangulo 2
    area2 = (ancho2 * alto2)
    return area2
    
def calcularPerimetro1(ancho1,alto1): #calcular perimetro del primero
    perimetro1 = ((2*ancho1)+(2*alto1))
    return perimetro1

def calcularPerimetro2(ancho2,alto2): #calcula el perimetro del triangulo 2
    perimetro2 = ((2*ancho2)+(2*alto2))
    return perimetro2
    
def calcularMayor(area1,area2):       #calcular el mayor de los triangulos
    if area1>area2 :
        areaMasGrande = "El primero"
    elif area1<area2:
        areaMasGrande = "El segundo"
    elif area1==area2:
        areaMasGrande = "Miden igual"
    return areaMasGrande  
    
def dibujarRectangulos(w,ancho1,alto1,ancho2,alto2):    #Dibuja los rectangulos que son representados
    
    Ancho1 = Line(150,(300 - ancho1))
    Ancho1.draw(W)
    Alto1 = Line((300 - alto1),150)
    Alto1.draw(W)
    Ancho2 = Line(300,(600 - ancho2))
    Ancho2.draw(W)
    Alto2 = Line((300 - alto2),600)
    Alto2.draw(W)
        
def main():
    w = Window(600,600)
    ancho1=int(input("Teclea el ancho del primer triángulo"))
    alto1=int(input("Teclea el alto del primer triángulo"))
    
    ancho2=int(input("Teclea el ancho del segundo tringulo"))
    alto2 = int(input("Tecle el alto del segundo triangulo"))

    area1 = calcularArea1(ancho1,alto1)
    area2 = calcularArea2(ancho2,alto2)
    perimetro1 = calcularPerimetro1(ancho1,alto1)
    perimetro2 = calcularPerimetro2(ancho2,alto2)
    mayor = calcularMayor(area1,area2)
    print("El area del primer triangulo es:", area1)
    print("El area del primer triangulo es:", area2)
    print("El perimetro del primer triangulo es:", perimetro1)
    print("El perimetro del segundo triangulo es:", perimetro2)
    print("El mayor de ambos es:", mayor)
    dibujarRectangulos(w,ancho1,alto1,ancho2,alto2)
main()