def conatarnotas(valor):
    for nota in (100,50,20,10,5,2):
        qtd = valor // nota
        valor = valor % nota
        if qtd > 0 :
            print(f'{qtd} nota(s) de r% {nota}')
            
#main
valor = float(input("qual o valor: "))
conatarnotas(valor)   
         