def validarSenha(s):
    if len(s) < 8:
        return 'senha invalida, muito curta.'
    
    temNumero = False
    temMaiuscula = False
    for  c in s:
           if c == ' ':
               return 'Senha invalida não pode ter espaços'
           if c >= 'A' and c <= 'Z':
               temMaiuscula =  True
           if c in simbolos:
               temSimbolo = True
                 
if not temNumero:
    return ' senha invalida'
 #main
senha = input('Digite a senha: ')
r = validarSenha
print(r)
