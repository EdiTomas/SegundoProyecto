
cont=0
txt=""
def incrementarContador():
     global cont
     cont= cont+1
     return "%d" %cont   


class Node(): 
      pass
          
class S(Node):
      
      def __init__(self, Etiqueta,hijo1):
           self.Etiqueta=Etiqueta
           self.hijo1=hijo1    

      def imprimir(ident):
           self.hijo1.imprimir(""+ident)
           print(ident+"Nodo: "+ self.Etiqueta)
       
      def traducir(self):
           global txt
           id = incrementarContador()
           hijo1=self.hijo1.traducir()
           txt+= id+"[label="+self.Etiqueta+"]"+"\n\t"
           txt+= id+"->"+hijo1+"\n\t"
           return "digraph G {\n\t"+txt+"}"
      def Resultado(self):
           return self.hijo1.Resultado()


class Entero(Node):
      def __init__(self,name):
           self.name=name
      
      def imprimir(ident):
          print(ident+"Nodo: "+ self.name)
      
      def traducir(self):
           global txt
           id = incrementarContador()
           txt+= id+"[label="+str(self.name)+ "]"+"\n\t"
           return id          
      def Resultado(self):
           return int(self.name)
      




class Suma(Node):
      def __init__(self,Etiqueta,hijo1,hijo2,hijo3):
           self.Etiqueta=Etiqueta
           self.hijo1=hijo1    
           self.hijo2=hijo2
           self.hijo3=hijo3

      def imprimir(ident):
           
           if type(self.hijo1)== type(tuple()):
                   self.hijo1[0].impirmir(""+ident) 
           else:             
                   self.hijo1.impirmir(""+ident) 
           
           print(ident+"Nodo: "+ self.hijo2)

           if type(self.hijo3)== type(tuple()):
                   self.hijo3[0].impirmir(""+ident) 
           else:             
                   self.hijo3.impirmir(""+ident)
                    
           print(ident+"Nodo: "+ self.Etiqueta)

      def traducir(self):
           global txt
           txt=""
           id = incrementarContador()
           
           if type(self.hijo1)== type(tuple()):
               hijo1 = self.hijo1[0].traducir() 
           else:             
               hijo1 = self.hijo1.traducir() 
               
           if type(self.hijo3)== type(tuple()):
               hijo3 = self.hijo3[0].traducir() 
           else:             
               hijo3 = self.hijo3.traducir() 
           txt+= id+"[label="+self.Etiqueta+"]"+"\n\t"
           txt+= id+"->"+hijo1+"\n\t"
           txt+= id+"[label="+ "\""+self.hijo2+"\""  +"]" +"\n\t"
           txt+= id+"->"+hijo3 +"\n\t"
           return id
      def Resultado(self):
           return self.hijo1.Resultado()+self.hijo3.Resultado()
           
       






class Resta(Node):
      def __init__(self, Etiqueta,hijo1,hijo2,hijo3):
           self.Etiqueta=Etiqueta
           self.hijo1=hijo1    
           self.hijo2=hijo2
           self.hijo3=hijo3
      def imprimir(ident):
           
           if type(self.hijo1)== type(tuple()):
                   self.hijo1[0].impirmir(""+ident) 
           else:             
                   self.hijo1.impirmir(""+ident) 
           
           print(ident+"Nodo: "+ self.hijo2)
           if type(self.hijo3)== type(tuple()):
                   self.hijo3[0].impirmir(""+ident) 
           else:             
                   self.hijo3.impirmir(""+ident)
           
           print(ident+"Nodo: "+ self.Etiqueta)
      
      def traducir(self):
           global txt
           id = incrementarContador()
           
           if type(self.hijo1)== type(tuple()):
                hijo1 = self.hijo1[0].traducir() 
           else:             
                hijo1 = self.hijo1.traducir() 
           
           
           if type(self.hijo3)== type(tuple()):
                  hijo3 = self.hijo3[0].traducir() 
           else:             
                  hijo3 = self.hijo3.traducir() 
           
           txt+= id+"[label="+self.Etiqueta+"]"+"\n\t"
           txt+= id+"->"+hijo1+"\n\t"
           txt+= id+"[label="+ "\""+self.hijo2+"\""  +"]" +"\n\t"
           txt+= id+"->"+hijo3+"\n\t"
           return id
      def Resultado(self):
           return self.hijo1.Resultado()-self.hijo3.Resultado()
      




class Multiplicacion(Node):
      def __init__(self, Etiqueta,hijo1,hijo2,hijo3):
           self.Etiqueta=Etiqueta
           self.hijo1=hijo1    
           self.hijo2=hijo2
           self.hijo3=hijo3
      
      def imprimir(ident):
           
           if type(self.hijo1)== type(tuple()):
                   self.hijo1[0].impirmir(""+ident) 
           else:             
                   self.hijo1.impirmir(""+ident) 
           
           print(ident+"Nodo: "+ self.hijo2)
           if type(self.hijo3)== type(tuple()):
                   self.hijo3[0].impirmir(""+ident) 
           else:             
                   self.hijo3.impirmir(""+ident)
           
           print(ident+"Nodo: "+ self.Etiqueta)

          



      def traducir(self):
           global txt
           id = incrementarContador()
           
           if type(self.hijo1)== type(tuple()):
                  hijo1 =  self.hijo1[0].traducir() 
           else:             
                  hijo1 =  self.hijo1.traducir() 
           
           
           if type(self.hijo3)== type(tuple()):
                  hijo3 = self.hijo3[0].traducir() 
           else:             
                  hijo3 = self.hijo3.traducir() 
           
           txt+= id+"[label="+self.Etiqueta+"]"+"\n\t"
           txt+= id+"->"+hijo1+"\n\t"
           txt+= id+"[label="+ "\""+self.hijo2+"\""  +"]" +"\n\t"
           txt+= id+"->"+hijo3+"\n\t"
           return id
      def Resultado(self):
           return self.hijo1.Resultado()*self.hijo3.Resultado()
      



class Division(Node):        
      def __init__(self, Etiqueta,hijo1,hijo2,hijo3):
           self.Etiqueta=Etiqueta
           self.hijo1=hijo1    
           self.hijo2=hijo2
           self.hijo3=hijo3  
      def imprimir(ident):
           
           if type(self.hijo1)== type(tuple()):
                   self.hijo1[0].impirmir(""+ident) 
           else:             
                   self.hijo1.impirmir(""+ident) 
           
           print(ident+"Nodo: "+ self.hijo2)

           if type(self.hijo3)== type(tuple()):
                   self.hijo3[0].impirmir(""+ident) 
           else:             
                   self.hijo3.impirmir(""+ident)
           
           print(ident+"Nodo: "+ self.Etiqueta)

      def traducir(self):
           global txt
           id = incrementarContador()
           
           if type(self.hijo1)== type(tuple()):
                hijo1 =    self.hijo1[0].traducir() 
           else:             
                hijo1 =    self.hijo1.traducir() 
           
           
           if type(self.hijo3)== type(tuple()):
                  hijo3 = self.hijo3[0].traducir() 
           else:             
                  hijo3 = self.hijo3.traducir() 
           
           txt+= id+"[label="+self.Etiqueta+"]"+"\n\t"
           txt+= id+"->"+hijo1+"\n\t"
           txt+= id+"[label="+ "\""+self.hijo2+"\""  +"]" +"\n\t"
           txt+= id+"->"+hijo3+"\n\t"
           
           return id
      
      def Resultado(self):
           return self.hijo1.Resultado()/self.hijo3.Resultado()
      
        


class Pa_Entero_PC(Node):
       def __init__(self, Etiqueta,hijo):
           self.Etiqueta=Etiqueta
           self.hijo=hijo    
       
       def imprimir(ident):
           
           if type(self.hijo)== type(tuple()):
                   self.hijo[0].impirmir(""+ident) 
           else:             
                   self.hijo.impirmir(""+ident) 
           
           print(ident+"Nodo: "+ self.Etiqueta)

       def traducir(self):
           global txt
           id = incrementarContador()
           
           if type(self.hijo)== type(tuple()):
                hijo =   self.hijo[0].traducir() 
           else:             
                hijo =   self.hijo.traducir() 
           
           #txt+= id+"[label="+ self.Etiqueta +"]"+"\n\t"
           txt+= id+"->"+hijo+"\n\t"
           return id
       def Resultado(self):
           return self.hijo.Resultado()
        
