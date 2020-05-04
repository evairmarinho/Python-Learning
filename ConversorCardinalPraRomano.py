import os

#lista necessária para convertemos números até a variável limite-1
romanos=['','I','II', 'III', 'IV', 'V' ,'VI' ,'VII', 'VIII','IX','X','L','C','D','M'] 

limite=4000

#convete qualquer número até limite-1 para romano
def paraRomano(n): 
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
        elif n<4000:
            return romanos[14]+romanos[14]+romanos[14]+paraRomano(n-3000)
        cont += 1
        
#chama o menu principal do usuário
def main():
    print("\nDigite uma opção\n")
    print("1 - Converter um número cardinal\n")
    print("2 - Converter uma data\n")
    print("3 - Visualizar uma soma em romano\n")
    print("4 - Finalizar o programa\n")
    escolha=int(input())
    if escolha==1:
        paraRomanoUsuario()
        os.system('cls')
        main()
    elif escolha==2:
        dataParaRomanoUsuario()
        os.system('cls')
        main()
    elif escolha==3:
        somaRomano()
        os.system('cls')
        main()
    elif escolha==4:
        print ("Programa Finalizado!")
        return 1
                
    else:
        print("Opção inválida")
        main()

#valida se o número tem a possibilidade de ser convertido para romano
def validador(n):
    if n==0:
        print('Não existe em romanos o 0!\n')
        main()
    elif n<0:
        print('Apenas números positivos!\n')
        main()
    elif n>=limite:
        print("Conversor suporta conversão até o número "+str(limite-1)+"\n")
        main()


#converte uma data
def dataParaRomano (dia,mes,ano):
    if (dia>0 and dia<32)and (mes>0 and mes<13):
        if mes==2:
                if ano%4==0 and (ano%100!=0 or (ano%100==0 and ano%400==0)):
                    if dia<30:
                         return paraRomano(dia)+"/"+paraRomano(mes)+"/"+paraRomano(ano) 
                    else:
                        print("Fevereiro possui apenas 29 dias\n")
                        return dataParaRomanoUsuario()
                elif dia==29:
                    print("O ano "+str(ano)+" não é bissexto\n")
                    return dataParaRomanoUsuario()
                elif dia<29:
                    return paraRomano(dia)+"/"+paraRomano(mes)+"/"+paraRomano(ano) 
                else:
                    print("Fevereiro possui apenas 28 dias\n")
                    return dataParaRomanoUsuario()
        if mes==2 or mes==4 or mes==6 or mes== 9 or mes==11:
            if dia<=30:
                return paraRomano(dia)+"/"+paraRomano(mes)+"/"+paraRomano(ano)
            else:
                print("O mês "+str(mes)+" possui "+str(dia-1)+" dias\n")
                return dataParaRomanoUsuario()
            
        return paraRomano(dia)+"/"+paraRomano(mes)+"/"+paraRomano(ano)
    else:
        print("Dia ou mês inválido!!!\n")
        return dataParaRomanoUsuario()


#interação I/O com usuário para converter a data escolhida
def dataParaRomanoUsuario():
    print('Digite uma data:\n')
    print('Digite o dia')
    dia =int(input())
    validador(dia)
    print('Digite o mês(Número)')
    mes =int(input())
    validador(mes)
    print('Digite o ano')
    ano =int(input())
    validador(ano)
    if(dataParaRomano(dia,mes,ano)!=None):
        print("A data "+str(dia)+"/"+str(mes)+"/"+str(ano)+" é igual a "+dataParaRomano(dia,mes,ano)+" em romano!\n")
        print("Digite 1 para converter mais uma data")
        escolha=int(input())
        if(escolha==1):
            dataParaRomanoUsuario()
        

#interage via I/O com usuário para converter o cardinal escolhido
def paraRomanoUsuario():
    print("Digite o número cardinal:")
    num=int(input())
    validador(num)
    print("O número cardinal "+str(num)+" é "+paraRomano(num)+" em romano!\n")
    print("Digite 1 para converter mais um número")
    escolha=int(input())
    if(escolha==1):
        paraRomanoUsuario()


#converte o resultado de uma soma
def somaRomano():
    soma=0
    print("Digite o primeiro valor:")
    num1=int(input())
    soma+=num1
    while(1):
        print("Digite o próximo valor")
        num2=int(input())
        soma+=num2
        print("Soma "+str(soma))
        print("Deseja continuar (1 para SIM)")
        escolha=int(input())
        if escolha!=1:
            print("Soma em romano: "+paraRomano(soma)+"\n")
            return 0  


print("------CONVERSOR PARA NÚMEROS ROMANOS(ATÉ "+str(limite-1)+")"+"------\n")
main()
