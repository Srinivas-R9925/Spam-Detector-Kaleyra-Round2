from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter.scrolledtext import ScrolledText

from NLP import Predict_A_Message

def reset_func():
    MessageBox.delete("1.0","end")
    
    
def verify_func():
    
    Message = MessageBox.get("1.0","end")
        
    check_spam = Predict_A_Message(Message)
        
    if(check_spam==1):
        root1 = Toplevel(root)
        root1.title("SPAM MESSAGE !")
        root1.geometry("1000x600+175+50")
        #isASpamIMG = ImageTk.PhotoImage(Image.open("InValid.png"))
        isASpamLabel = Label(root1, image = isASpamIMG)
        isASpamLabel.place(x=0,y=0)

    elif(check_spam==0):
        root2 = Toplevel(root)
        root2.title("VALID MESSAGE !")
        root2.geometry("1000x600+175+50")
        #notASpamIMG = ImageTk.PhotoImage(Image.open("Valid.png"))
        notASpamLabel = Label(root2, image = notASpamIMG)
        notASpamLabel.place(x=0,y=0)
        

root = Tk()
root.resizable(False, False)
root.geometry("1000x600+175+50")
root.title("Spam Guard")

isASpamIMG = ImageTk.PhotoImage(Image.open("InValid.png"))
notASpamIMG = ImageTk.PhotoImage(Image.open("Valid.png"))

logo = ImageTk.PhotoImage(Image.open("LOGO.png"))
logoimg = Label(root,image=logo)
logoimg.place(x=260, y=60)
        
enter_label = Label(root, text="Please Enter the Message to verify for SPAM : ",fg="black",font=('Times New Roman',24,'bold'))
enter_label.place(x =150, y = 200)
        
MessageBox = Text(root, font=("Arial 20"),  width = 45,  height = 7)
Message = MessageBox.get("1.0","end")
MessageBox.place(x =150, y = 250)
        
reset_button = Button(root, text="CLEAR", bd=4,bg='powderblue',width = 10,  height = 1, font=('Times New Roman',20,'bold'), command=reset_func)
reset_button.place(x =230, y = 495)
        
verify_button = Button(root, text="VERIFY", bd=4,bg='powderblue',width = 10,  height = 1, font=('Times New Roman',20,'bold'), command=verify_func)
verify_button.place(x =550, y = 495)
        
root.mainloop()