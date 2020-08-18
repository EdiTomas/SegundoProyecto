from tkinter import *
from NumerosPrimos import*
import gramatica as g
from Nodo import *
import os
from graphviz import render
def iniciar():
     window=Tk()
     window.title("Calculadora con un Analizador")
     window.geometry("650x450")
     window.config(bg="#FFB266")

     entrada=StringVar() 
     texto =Text(window,width=60,height=10)
     texto.grid(row=1, column=1,padx=40,pady=10) 
     scrollVert=Scrollbar(window,command=texto.yview)
     scrollVert.grid(row=1,column=2,sticky="nsew")
     texto.config(yscrollcommand=scrollVert.set)
     
     consola =Text(window,width=60,height=10)
     consola.grid(row=3, column=1,padx=40,pady=5)
     scrollVert1=Scrollbar(window,command=consola.yview)
     scrollVert1.grid(row=3,column=2,sticky="nsew")
     consola.config(yscrollcommand=scrollVert1.set)
     # consola.tag_configure("red", foreground="red")
     # consola.highlight_pattern("word", "red")


     def codigoBoton():
       consola.delete(1.0,'end')
       contenido = texto.get(1.0, 'end')     
       nod= Node()  
       nod=g.Analizador(str(contenido))
       consola.insert(INSERT,str(nod.Resultado())+"\n")
       CrearArchivo(str(nod.traducir()))
       #render('dot', 'Tjpg','arbol.dot','-O', 'arbol.jpg') 
       render('dot','jpg','arbol.dot') 
     
     def CrearArchivo(contenido):
        file = open("arbol.dot", "w")
        file.write(contenido)
        file.close() 

     
     
     ejecutar = Button(window,text="analizar",width=10,height=1,  command=codigoBoton)
     ejecutar.grid(row=2, column=1,padx=10,pady=10) 
     ejecutar.config(bg="blue")       
     

     window.mainloop()




