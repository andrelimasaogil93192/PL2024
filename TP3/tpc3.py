soma = 0
controler = True
while(True):
    frase = input("\n")
    i = 0
    while i<len(frase):
        if(frase[i].isdigit()):
            if controler:
                if frase[i].isdigit() and i<len(frase): 
                    soma += int(frase[i])
                    i += 1
            else: 
                i += 1
            

        elif frase[i] == "=":
            print(soma)
            i+=1

        elif frase[i:i+3].lower() == "off":
            controler = False
            i +=3
        elif frase[i:i+2].lower() == "on":
            controler = True
            i+=2
        else:
            i += 1
       
        
        
 
        
    1


        