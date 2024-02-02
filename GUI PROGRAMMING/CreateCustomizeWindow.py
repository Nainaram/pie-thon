# #import Tkinter
# from tkinter import *
# #creating a  main method
# r = Tk()
# r.geometry("500x500")
# r.title("FACEBOOK")
# r.config(bg = "blue")
# # main loopmehtod called
# mainloop()
#Adding widgets to window
#import Tkinter
from tkinter import *
#creating a  main method
r = Tk()
r.geometry("500x500")
r.title("FACEBOOK")
r.config(bg = "blue")

rn = Label(r,text='Roll No')
rn.place(x=20,y =20)
fn= Label(r,text='FirstName')
fn.place(x=20,y =60)
ln = Label(r,text='LastName')
ln.place(x=20,y =100)
em = Label(r,text='Email')
em.place(x=20,y =160)

#ADDING ENTRY BOXES INTO MAIN WINDOW
ern = Entry()
ern.place(x=100,y =20)
efn = Entry()
efn.place(x=100,y =60)
eln = Entry()
eln.place(x=100,y =100)
eem = Entry()
eem.place(x=100,y =160)

#adding buttons into main window
button1 = Button(r,text="Button1",bg="white")
button1.place(x=20,y=200)
# main loopmehtod called
mainloop()