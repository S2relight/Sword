# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:22:48 2019

@author: User
"""
import time
j=["C","A","F","E","T","E","R","I","A"," ","O","P","E","N","I","N","G"," "]
for c in range(0,len(j)):
    print("\n"*30)
    for k in range(0,c):
        
        print(" "*5, j[k],end="")
        
     
    print("\n"*20)
    
    time.sleep(0.2)
print()
#print "\n"*50
print("""
                ************    ***********       ***********
                ************    ***********      *************
                ****      **       ****         ****
                ****      **       ****        ****
                ***********        ****        ****
                ***********        ****        ****    ********
                ***********        ****        ****    ********
                ****     ***       ****        ****        ****
                ****     ***       ****        ****        ****
                ***********     ***********     ***************
                **********      ***********      *************
      """)



import tkinter
from tkinter import *

from tkinter import messagebox

list=[]




def tex():
    sinem=sum(list)*0.12
    sam=sinem+sum(list)
    
    return sam
    

def GST():
    def Calculate_GST(org_cost, N_price): 
  
        # return value after calculate GST% 
        return (((N_price - org_cost) * 100) / org_cost); 
  
    # Driver program to test above functions 
    org_cost = sum(list)
    N_price = tex()
    print("GST = ",end='') 
  
    print(round(Calculate_GST(org_cost, N_price),2),end='') 
  
    print("%") 


def add():
    data=Lb.get(ACTIVE)
    if data=='Sprite 41/-':
        tb.insert(END,'\nSprite\t41 x %d'%(qnt.get()))
        list.append(41*qnt.get())

    elif data=='Pepsi 41/-':
        tb.insert(END,'\nPepsi\t41 x %d'%(qnt.get()))
        list.append(41*qnt.get())

    elif data=='DietCoke  65/-':
        tb.insert(END,'\nDietCoke\t65 x %d'%(qnt.get()))
        list.append(65*qnt.get())

    elif data=='Mojito 145/-':
        tb.insert(END,'\nMojito\t145 x %d'%(qnt.get()))
        list.append(145*qnt.get())
        
    elif data=='Cappuccino 162/-':
        tb.insert(END,'\nCappuccino\t162 x %d'%(qnt.get()))
        list.append(162*qnt.get())
        
    elif data=='Fanta 41/-':
        tb.insert(END,'\nFanta\t41 x %d'%(qnt.get()))
        list.append(41*qnt.get())
        
    elif data=='CocoCola 38/-':
        tb.insert(END,'\nCocaCola\t38 x %d'%(qnt.get()))
        list.append(38*qnt.get())
        
    elif data=='ColdCoffee 150/-':
        tb.insert(END,'\nColdCoffee\t150 x %d'%(qnt.get()))
        list.append(150*qnt.get())
        
    elif data=='HotDog 49/-':
        tb.insert(END,'\nHotDog\t49 x %d'%(qnt.get()))
        list.append(49*qnt.get())
    
    elif data=='VegBurger 55/-':
        tb.insert(END,'\nVegBurger\t55 x %d'%(qnt.get()))
        list.append(55*qnt.get())
    
    elif data=='Pasta 180/-':
        tb.insert(END,'\nPasta\t180 x %d'%(qnt.get()))
        list.append(180*qnt.get())
    
    elif data=='HamBurger 62/-':
        tb.insert(END,'\nHamBurger\t62 x %d'%(qnt.get()))
        list.append(62*qnt.get())
        
    elif data=='Sandwitch 45/-':
        tb.insert(END,'\nSandwitch\t45 x %d'%(qnt.get()))
        list.append(45*qnt.get())
        
    elif data=='Spaghetti 150/-':
        tb.insert(END,'\nSpaghetti\t150 x %d'%(qnt.get()))
        list.append(150*qnt.get())
        
    elif data=='FrenchFries 118/-':
        tb.insert(END,'\nFrenchFries\t118 x %d'%(qnt.get()))
        list.append(118*qnt.get())
        
    elif data=='Fazitas 180/-':
        tb.insert(END,'\nFazitas\t180 x %d'%(qnt.get()))
        list.append(180*qnt.get())
    
        
def rem(GST,tex):
    return("Original Amount:",sum(list),"\n"*4,"Final Amount:",tex())
    

    
def total():
    c=rem(GST,tex)
    messagebox.showinfo("Hello %s"%(nameinfo.get()),c)

def clr():
    tb.delete(1.0,END)
    list.clear()

f=Tk()
f.title("BIG")

nameinfo=StringVar()
data=IntVar()
qnt=IntVar()

name=Label(f,text='Name :')
e1=Entry(f,width=20,bd=3,textvariable=nameinfo)

prod=Label(f,text='Products :',bd=3)
Lb=Listbox(f,height=15,width=30,bd=3)
Lb.insert(0,'Items Price\n')
Lb.insert(1,"")
Lb.insert(2,'Sprite 41/-')
Lb.insert(3,'DietCoke 65/-')
Lb.insert(4,'Mojito 145/-')
Lb.insert(5,'Cappucinno 162/-')
Lb.insert(6,'Fanta 41/-')
Lb.insert(7,'CocaCola 38/-')
Lb.insert(8,'ColdCoffee 150/-')
Lb.insert(9,'HotDog 49/-')
Lb.insert(10,'VegBurger 55/-')
Lb.insert(11,'Pasta 180/-')
Lb.insert(12,'Hamburger 62/-')
Lb.insert(13,'Sandwitch 45/-')
Lb.insert(14,'Spaghetti 150/-')
Lb.insert(15,'FrenchFries 118/-')
Lb.insert(16,'Fazitas 180/-')

quan=Label(f,text='Quantity :')
e2=Entry(f,width=15,bd=3,textvariable=qnt)

b1=Button(f,text='Add Items',width=12,bd=3,command=add)

tb=Text(f,height=5,width=20,bd=3)

b3=Button(f,text='Clear Items',width=12,bd=3,command=clr)

b2=Button(f,text='Total',width=12,bd=3,command=total)

name.grid(row=0,column=0,padx=5,pady=5)
e1.grid(row=0,column=1,padx=5,pady=5)
prod.grid(row=1,column=0,padx=5,pady=5)
Lb.grid(row=1,column=1,padx=5,pady=5)
quan.grid(row=2,column=0,padx=5,pady=5)
e2.grid(row=2,column=1,padx=5,pady=5)
b1.grid(row=3,column=1,padx=5,pady=5)
tb.grid(row=4,columnspan=2,padx=5,pady=5)
b3.grid(row=5,column=0,padx=5,pady=5)
b2.grid(row=5,column=1,padx=5,pady=5)

f.mainloop()
