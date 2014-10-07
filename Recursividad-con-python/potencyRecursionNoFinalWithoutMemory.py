# Jose Enrique Ruiz Navarro
# email- joseenriqueruiznavarro@gmail.com
#http://www.systerminal.com
# -*- encoding: utf-8 -*-

def potenciaNoFinal(base,exponente):
    # base case
    if(exponente==0):
        result=1
    else:
        result = base*potenciaNoFinal(base,exponente-1)
    # For example : 2^3 =2*2*2*1
    # multiply the base until the exponent is 0 which multiply by 1 in the final case
    return result




def main():
    # enter base
    base = int(input("Introduce la base: "))
    # enter exponent
    exponente=int(input("Introduce el exponente: "))
    res = potenciaNoFinal(base,exponente)
    # print result
    print(res)



if __name__ == "__main__":
    main()
