# --------- RECEBENDO INFORMAÇÕES --------- #

num = int(input("Aperte '1' para codificar uma mensagems ou aperte '2' para decodificar uma mensagem: "))
avanca = 3
cripto = " "
decripto = " "
abc = "abcdefghijklmnopqrstuvwxyz"
cba = "zyxwvutsrqponmlkjihgfedcba"

# --------- CODIFICANDO --------- #
if(num == 1):
    mes = input("Digite a mensagem para ser criptografada: ")
    mes = mes.lower()
    for i in (mes):
        posicao = abc.find(i)
        posicao = posicao + avanca
    
        if(posicao >= len(abc)):
            posicao = posicao - len(abc)
        cripto = cripto + abc[posicao]
    
    print("A mensagem criptografada será: " + cripto)

# --------- DECODIFIVANDO --------- #
elif(num == 2):
    mes = input("Digite a mensagem para ser decriptografada: ")
    mes = mes.lower()
    for i in(mes):
        inverco = cba.find(i)
        inverco = inverco + avanca

        if (inverco >= len(cba)):
            inverco = inverco - len(cba)
        decripto = decripto + cba[inverco]
    print("mensagem decriptografada é: " + decripto)

# --------- CONDIÇÃO FALSA --------- #
else:
    print("valor incorreto!")