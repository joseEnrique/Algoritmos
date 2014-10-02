#Jose Enrique Ruiz Navarro
#email- joseenriqueruiznavarro@gmail.com
#http://www.systerminal.com 
# -*- encoding: utf-8 -*-
#
#								| resultado     si numero=0
# factorial(numero,resultado)= 	|
#								|f(numero-1,numero*resultado) si numero>0

def factorialFinal(numero):
	if(numero<0):
		r=-1
	else:
		r=__factorialAux(numero,1)
	return r
	
def __factorialAux(numero,resultado):
	if (numero==0) or (numero==1):
		r=resultado
	else:
		r=__factorialAux(numero-1,resultado*numero)
	return r

def main():
	n=int(raw_input("Introduce el numero para el calculo: "))
	res=factorialFinal(n)
	if res != -1 :		
		print res
	else :
		print "El numero no puede ser negativo"
	
if __name__ == "__main__":
    main()
	
