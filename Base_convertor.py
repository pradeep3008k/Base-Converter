from tkinter import *
from tkinter.font import Font

root=Tk()
root.title("Base Convertor")
root.config(bg="black")

root.resizable(0,0)

def get_in():
    
    answer_box.delete(1.0,END)
    a=entry1.get()
    p=c1.get()
    q=c2.get()
    
    p=int(p)
    q=int(q)
    
    n=[]
    #now append all elements of string a in a the list n    
    for i in a:
        n.append(i)
    n_new=[]
    #now check whether there is a alphabet or not ,if yes than change it to its reference value
    #here reference values are like : 10 for A , 11 for B etc.
    for i in n:
        if i.isalpha()==False:
            n_new.append(i)
        if i.isalpha()==True:
            n_new.append(ord(i)-55)
    #as some of the integer elements of the list are in string format
    #so convert these into integer format        
    for i in range(len(n_new)):
        n_new[i]=int(n_new[i])
    
    x=len(n_new)
    num=[]
    # first convert the given number in decimal
    for i in range(x):
        n_new[i]=n_new[i]*(p**(x-i-1))
        num.append(n_new[i])    
    print(num)    
    k=0            
    #now sum all the elements of num list to get the given number into decimal    
    for j in range(len(num)):
        k=k+num[j]    
    y=[]
    ans=[]
    #the algo is basically that divide the number(i.e already converted in decimal base) by the given base q  
    #and store the remainder in a new list and divide the quotient by base q again until you get 1    
    while k>=1:
        x=k%q
        y.append(x)
        k=k//q
    new=[]
    #now convert the elements of list(y) that are greater than 9 
    #into capital alphabets according to hexa decimal rules
    for i in y:
        if i<10:
            new.append(i)
        if i>9 and i<36:
            new.append(chr(i-10+65))
    #now the reverse the list to get actual answer
    new_rev=[]
    for i in range(len(new)):
        new_rev.append(new[-i-1])
    
    #now defne a function which will detect whether the given input is in given base or not        
    right=[]
    right_new=[]
    output=0
    for i in a:
        right.append(i)
    for i in right:
        if i.isalpha()==False:
            right_new.append(i)
        if i.isalpha()==True:
            right_new.append(ord(i)-55)
    
    for i in range(len(right_new)):
        right_new[i]=int(right_new[i])
    
    for i in right_new:
        if i>=p:
            output=output+1
            
    # now check whether the given input is in base p or not
    if output==0:
    #if yes than:
    #print the elements of the list joined together    
        for i in range(len(new_rev)):
            new_rev[i]=str(new_rev[i])
        s="".join(new_rev)

        answer_box.insert(INSERT,s)
    #if not than print error
    else:
        answer_box.insert(INSERT,"Your input is not appropriate")
       
def clear_all():
    entry1.delete(0,END)
    answer_box.delete(1.0,END)
    c1.set("select")
    c2.set("select")  

#---------------------Font------------------------

default_font=Font(size=16)
button_font=Font(size=14)

#---------------------LABELS------------------------

input_label=Label(root,text="Input",fg="gold",bg="black",font=default_font)
input_label.place(x=46,y=20)

from_base_label=Label(root,text="From Base",fg="turquoise1",bg="black",font=default_font)
from_base_label.place(x=45,y=90)

to_base_label=Label(root,text="To Base",fg="gold",bg="black",font=default_font)
to_base_label.place(x=45,y=160)

answer=Label(root,text="Answer",fg="turquoise1",bg="black",font=default_font)
answer.place(x=45,y=230)


#-----------------Buttons---------------------------
convert_button=Button(root,text="Convert",font=button_font,bg="gold",command=get_in).place(x=50,y=350)
reset_button=Button(root,text="Reset",font=button_font,bg="gold",command=clear_all).place(x=310,y=350)


from tkinter.ttk import *

#-------------------ENTRY Box-----------------------

entry1=Entry(root,width=26,font=default_font)
entry1.place(x=50,y=50)

l1=list(range(2,37))
c1=Combobox(root,state="readonly",value=l1,width=25,font=default_font)
c1.set("select")
c1.place(x=50,y=120)


l2=list(range(2,37))
c2=Combobox(root,state="readonly",value=l2,width=25,font=default_font)
c2.set("select")
c2.place(x=50,y=190)

#-------------------Answer box----------------------

answer_box=Text(root,width=27,height=3,font=default_font)
answer_box.place(x=50,y=260)




root.geometry("450x420+200+200")
root.mainloop()
