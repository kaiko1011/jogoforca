#escolha da palavra
palavra = "abobora"
#criando a lista 
certo = list(" ".join(['_'*len(palavra)]))
status = " "
cont= 0
erros = 0
total = 0
repetida = 0
#Inicio do loop ate que palavra esteja completa
while cont < len(certo):
    palpite = input("Digite uma letra : ")
    # percorendo a palavra conforme tamanho desta
    for i in range(len(palavra)): 
        #se letra digitada tem na palvra mas nao esta na lista adiciona ela   
        if palpite in palavra[i]:
            if palpite != certo[i]: 
              del certo[i]
              certo.insert(i,palavra[i])   
              cont= cont + 1 
              status = "correto "
            #caso letra ja esteja na lista so atualiza e muda status
            else:
               status = ("letra repetida") 
               repetida = repetida + 1 
               break  
        elif palpite not in palavra: 
             status = "erro"
             erros = (erros + 1)  
    print(status)  
    print(str(certo).replace("," , " "))  
    total = (total  + 1 )
#erro dividido pelo tamanho da lista devido cada letra
    # percorrer todos indices desta
erros = erros /len(certo)            
print("\nParabens voçê acertou!!!!\n")
print(f"Voce errou  {erros:.0f}  vezes\n")
print(f"Repetiu {repetida} letras\n")
print(f"Num total de {total} jogadas.")          
          

        
                


            


