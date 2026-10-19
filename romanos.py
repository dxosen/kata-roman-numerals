algarismoI= [1, "i"]

def converter(numero):
    #variaveis

    resultado = ""
    
    tabela = [(1, 'I')]

    for valor, simbolo in tabela:
        
        enquanto_couber = numero // valor
        if enquanto_couber > 0:
            resultado += simbolo * enquanto_couber
            numero %= valor 
            
    return resultado


