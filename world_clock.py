#Libraries
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

#Root Window GUI
root=Tk()
root.geometry("1000x1000")

india = ImageTk.PhotoImage(Image.open ("india.jpg"))
usa = ImageTk.PhotoImage(Image.open ("usa.jpg"))
australia = ImageTk.PhotoImage(Image.open ("australia.jpg"))
japan = ImageTk.PhotoImage(Image.open ("japan.jpg"))

#India GUI
india_label = Label(root,text="India")
india_label.place(relx=0.2,rely=0.05,anchor=CENTER)

india_map=Label(root)
india_map['image']=india
india_map.place(relx=0.2,rely=0.35,anchor=CENTER)

india_time = Label(root)
india_time.place(relx=0.2,rely=0.55,anchor=CENTER)

#USA GUI
usa_label = Label(root,text="USA")
usa_label.place(relx=0.8,rely=0.05,anchor=CENTER)

usa_map=Label(root)
usa_map['image']=usa
usa_map.place(relx=0.8,rely=0.35,anchor=CENTER)

usa_time = Label(root)
usa_time.place(relx=0.8,rely=0.55,anchor=CENTER)

#Australia GUI
aus_label = Label(root,text="Australia")
aus_label.place(relx=0.2,rely=0.6,anchor=CENTER)

aus_map = Label(root)
aus_map['image']=australia
aus_map.place(relx=0.2,rely=0.78,anchor=CENTER)

aus_time = Label(root)
aus_time.place(relx=0.2,rely=0.95,anchor=CENTER)

#Japan GUI
jpn_label = Label(root,text="Japan")
jpn_label.place(relx=0.8,rely=0.6,anchor=CENTER)

jpn_map = Label(root)
jpn_map['image'] = japan
jpn_map.place(relx=0.8,rely=0.78,anchor=CENTER)

jpn_time = Label(root)
jpn_time.place(relx=0.8,rely=0.95,anchor=CENTER)

#India Class
class India():
    def time(self):
        home=pytz.timezone('Asia/Kolkata')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        india_time['text']="Time: "+current_time
        india_time.after(200,self.time)
        
#USA Class
class USA():
    def time(self):
        home=pytz.timezone('US/Pacific')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        usa_time['text']="Time: "+current_time
        usa_time.after(200,self.time)
        
#Australia Class
class aus():
    def time(self):
        home=pytz.timezone('Australia/ACT')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        aus_time['text']="Time: "+current_time
        aus_time.after(200,self.time)
        
#Japan Class
class Japan():
    def time(self):
        home=pytz.timezone('Japan')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        jpn_time['text']="Time: "+current_time
        jpn_time.after(200,self.time)

#Objects for all countries
obj_india = India()
obj_USA = USA()
obj_aus = aus()
obj_japan = Japan()

#India Button
btn1 = Button(root,text="Show Time",command=obj_india.time)
btn1.place(relx=0.2,rely=0.15,anchor=CENTER)

#USA Button
btn2 = Button(root,text="Show Time",command=obj_USA.time)
btn2.place(relx=0.8,rely=0.15,anchor=CENTER)

#Australia Button
btn3 = Button(root,text="Show Time",command=obj_aus.time)
btn3.place(relx=0.2,rely=0.63,anchor=CENTER)

#Japan Button
btn4 = Button(root,text="Show Time",command=obj_japan.time)
btn4.place(relx=0.8,rely=0.63,anchor=CENTER)

#Run Statement
root.mainloop()