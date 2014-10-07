#Jose Enrique Ruiz Navarro
#email- joseenriqueruiznavarro@gmail.com
#http://www.systerminal.com 
# -*- encoding: utf-8 -*-
def factorialNoFinal(numero):
	"""Function to return the factorial of a number using recursion not final and without memory"""	
	"""Funcion que devuelve el factorial de un numero usando recursion no final y sin memoria"""
	if numero >=0:
		if numero==0:
			r=1
		else:
			#Llamada recursiva
			r=numero * factorialNoFinal(numero-1)
	else:
		r=-1
	return r

def main():
	n=int(raw_input("Introduce el numero para el calculo: "))
	res=factorialNoFinal(n)
	if res != -1 :		
		print (res)
	else :
		print ("El numero no puede ser negativo")
	
if __name__ == "__main__":
    main()
    
		
	
	
