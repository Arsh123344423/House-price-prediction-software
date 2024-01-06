from tkinter import *
import customtkinter as ck
import mysql.connector 
import tkinter.messagebox as TKM
from PIL import Image
l=[]
l1=[]
avg=0
rate=0
def GUI():
    def call_userinterface():
        def get_entry():
            global l
            l= [City_entry.get(),Year_entry.get()]
            root.destroy()
        root=ck.CTk()
        ck.set_appearance_mode("black")
        root.maxsize(650,350)
        root.geometry("650x350")
        City=ck.CTkLabel(master=root,text="City:", font=("TkDefaultFont", 30))
        City.place(relx=0.35,rely=0.35,anchor=CENTER)
        City_entry=ck.CTkEntry(master=root,placeholder_text="City",width=160,height=27)
        City_entry.place(relx=0.6,rely=0.36,anchor=CENTER)
        Year=ck.CTkLabel(master=root,text="Year:", font=("TkDefaultFont", 30))
        Year.place(relx=0.35,rely=0.5,anchor=CENTER)
        Year_entry=ck.CTkEntry(master=root,placeholder_text="Year",width=160,height=27)
        Year_entry.place(relx=0.6,rely=0.5,anchor=CENTER)
        button=ck.CTkButton(master=root,text="Submit",height=40,width=100,command= get_entry )
        button.place(relx=0.50,rely=0.70,anchor=CENTER)
        root.mainloop()
    def Gif():
        c=0
        root=Tk()
        img="2GU.gif"
        root.title("Loading....")
        root.maxsize(650,600)
        root.configure(bg="black", width=650, height=350)
        root.geometry("650x600")
        openImage=Image.open(img)
        frames=openImage.n_frames
        imageObject=[PhotoImage(file=img,format=f"gif -index {i}")for i in range(frames)]
        count=0
        showAnimation=None
        def animation(count):
            newImage=imageObject[count]
            gif_Label.configure(image=newImage)
            count+=1
            if count == frames:
                root.destroy()
            showAnimation=root.after(50,lambda:animation(count))
        gif_Label=Label(root,image="",text="Loading.....")
        gif_Label.place(x=100,y=40,width=450,height=500)
        animation(count)
        root.mainloop()
        c+=1
    call_userinterface()
    Gif()
    print(l)
GUI()
def connector():
    global avg
    global rate
    global l1
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="krrish1234",database="city")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM city1 where city=%s;",(l[0],))
    myrecords=mycursor.fetchone()
    avg=myrecords[1]
    rate=myrecords[2]
    mydb.close()
def princple():
    A=0
    global l
    global avg
    global rate
    def Gif2():
        c=0
        root=Tk()
        img="2GU.gif"
        root.title("Loading....")
        root.maxsize(650,600)
        root.configure(bg="black", width=650, height=350)
        root.geometry("650x600")
        openImage=Image.open(img)
        frames=openImage.n_frames
        imageObject=[PhotoImage(file=img,format=f"gif -index {i}")for i in range(frames)]
        count=0
        showAnimation=None
        def animation(count):
            newImage=imageObject[count]
            gif_Label.configure(image=newImage)
            count+=1
            if count == frames:
                root.destroy()
            showAnimation=root.after(50,lambda:animation(count))
        gif_Label=Label(root,image="",text="Loading.....")
        gif_Label.place(x=100,y=40,width=450,height=500)
        animation(count)
        root.mainloop()
        c+=1
    Gif2()
    f=[int(avg),float(rate),eval(l[1])-2023]
    A=(f[0]*pow((1+f[1]/100),f[2]))
    TKM.showinfo("Output",A)
while True:
    if l[0].isalpha()==False and l[1].isnumeric()==False:
        TKM.showerror("Invalid Values!","Both the values contain invalid character")
        GUI()
    elif l[0].isalpha()==False:
        TKM.showerror("Invalid Value!","Please enter ONLY Alphabets in place of City")
        GUI()
    elif l[1].isnumeric()==False:
        TKM.showerror("Invalid Value!","Please enter ONLY Numbers in the place of Year")
        GUI()
    else:
        TKM.showinfo("Valid INPUT!!!","THANK YOU!!!")
        break
connector()
princple()

