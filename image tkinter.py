from tkinter import *
import sys
sys.path.append("C:/users/abinaya/appdata/roaming/python/python311/site-packages")

from PIL import ImageTk, Image

root=Tk()
root.title("photo gallery")
#RE= "C:\Users\Abinaya\Downloads\2021-Himalayan-Royal-Enfield-7.jpg"
#javascript ="D:\Tkinter\javascript-logo.png"
#Python=
#Django="D:\Tkinter\django-python-logo.png"
#flask="D:\Tkinter\flask-logo-black-and-white.png"
javascript_image = ImageTk.PhotoImage(Image.open("D:\Tkinter\javascript-logo.png"))
django_image=ImageTk.PhotoImage(Image.open("D:\Tkinter\django-python-logo.png"))
#flask_image=ImageTk.PhotoImage(Image.open("D:\Tkinter\flask-logo-png-transparent.png"))
RE_image=ImageTk.PhotoImage(Image.open("D:\\Tkinter\\2021-Himalayan-Royal-Enfield-7.jpg"))
def back(index):
    global my_label 
    global back_button
    global next_button

    if index==0:
        return
    my_label.grid_forget()
    my_label=Label(image=images_list[index-1])
    my_label.grid(row=0, column=0,columnspan=3)

    back_button=Button(root,text="Back",command=lambda:back(index-1))
    next_button=Button(root,text="Next",command=lambda:next(index+1))

    back_button.grid(row=1,column=0)
    next_button.grid(row=1,column=1)
    return
def next(index):
    global my_label 
    global back_button
    global next_button

    if index==2:
        return
    my_label.grid_forget()
    my_label=Label(image=images_list[index+1])
    my_label.grid(row=0, column=0,columnspan=3)

    back_button=Button(root,text="Back",command=lambda:back(index-1))
    next_button=Button(root,text="Next",command=lambda:next(index+1))

    back_button.grid(row=1,column=0)
    next_button.grid(row=1,column=1)
    return

images_list=[javascript_image,django_image,RE_image]         

my_label=Label(image=images_list[0])
my_label.grid(row=0, column=0,columnspan=3)

back_button=Button(root,text="Back",command=lambda:back(0))
next_button=Button(root,text="Next",command=lambda:next(0))
exit_button=Button(root,text="Exit",command=root.quit)

back_button.grid(row=1,column=0)
next_button.grid(row=1,column=1)
exit_button.grid(row=1,column=2)

root.mainloop()
