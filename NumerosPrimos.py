def NumeroPrimo(numero):
    n=2
    milista=[]   
    while n<numero:    
        contador =0 
        for x in range(1,n):
            if(n%x==0):
                 contador = contador+1                               
               
        if(contador==1):
           milista.append(n) 
           print("Es numero primo",n);     
        
        n=n+1  
    return milista    

