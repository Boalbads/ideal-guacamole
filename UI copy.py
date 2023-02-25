from tkinter import *
import random
import time

jackpotamount = "£25,000,000"

class MyWindow:
    spinning = True
    def __init__(self, win): # self and window?
        self.lbl1=Label(win, text='0', font=("Arial", 40))
        self.lbl2=Label(win, text='0', font=("Arial", 40))
        self.lbl3=Label(win, text='0', font=("Arial", 40))
        self.lbl4=Label(win, text='', font=("Arial", 25))
        self.lbl1.place(x=100, y=75) # no size so it makes size based on text length
        self.lbl2.place(x=140, y=75) # no size so it makes size based on text length
        self.lbl3.place(x=180, y=75) # no size so it makes size based on text length
        self.lbl4.place(x=50, y=130) # no size so it makes size based on text length
        self.b1=Button(win, text='Spin', command=self.spin)
        #self.b2=Button(win, text='Press at correct time!', command=self.clik)
        self.b1.place(x=100, y=50) # no size so it makes size based on text length
        #self.b2.place(x=100, y=140) # no size so it makes size based on text length
    def spin(self):
        eee = str(random.randrange(100, 999, 1))
        ee = list(eee)
        self.lbl1["text"]=str(ee[0])
        self.lbl2["text"]=str(ee[1])
        self.lbl3["text"]=str(ee[2])

        if self.lbl1["text"] == self.lbl2["text"] and self.lbl2["text"] == self.lbl3["text"]:
            winstatement = "You win "+jackpotamount+"! \nTry again to perhaps earn more..?"
            self.lbl4["text"]=winstatement
            print("Win!")
        else:
            self.lbl4["text"]="You lose, try again."
            

window=Tk()
mywin=MyWindow(window)
window.title('Hello Python - This is a slot machine :=)')
window.geometry("640x480+10+10") #XSIZExYSIZE+XPOS+YPOS
window.mainloop()
