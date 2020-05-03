
romanos=['','I','II', 'III', 'IV', 'V' ,'VI' ,'VII', 'VIII','IX','X','L','C','D','M'] #lista necessária para convertemos números até 2999

limite=2999
def paraRomano (n):
    cont = 0
    for i in romanos:
        if n==0:
            return romanos[0]
        if n>=1 and n<=10:
            if cont == n:
                return i
        elif n<40:
            return romanos[10]+paraRomano(n-10)
        elif n<50:
            return romanos[10]+romanos[11]+paraRomano(n-40)
        elif n<90:
            return romanos[11]+paraRomano(n-50)
        elif n<100:
            return romanos[10]+romanos[12]+paraRomano(n-90)
        elif n<400:
            return romanos[12]+paraRomano(n-100)
        elif n<500:
            return romanos[12]+romanos[13]+paraRomano(n-400)
        elif n<900:
            return romanos[13]+paraRomano(n-500)
        elif n<1000:
            return romanos[12]+romanos[14]+paraRomano(n-900)
        elif n<1500:
            return romanos[14]+paraRomano(n-1000)
        elif n<1900:
            return romanos[14]+romanos[13]+paraRomano(n-1500)
        elif n<2000:
            return romanos[14]+romanos[12]+romanos[14]+paraRomano(n-1900)
        elif n<3000:
            return romanos[14]+romanos[14]+paraRomano(n-2000)
        cont += 1
        

def inicio():
    print("Digite o número cardinal:")
    num=int(input())
    if(num==0):
        print('Não existe em romanos o 0!\n')
        inicio()
    elif num<0:
        print('Apenas números positivos!\n')
        inicio()
    else:
        print("O número cardinal "+str(num)+" é "+paraRomano(num)+" em romano!")

print("------CONVERSOR DE NÚMEROS CARDINAIS PARA NÚMEROS ROMANOS(ATÉ 2999)------\n")
inicio()
