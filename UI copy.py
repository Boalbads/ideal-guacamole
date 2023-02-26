from tkinter import *
import random
import time
import threading

jackpotsquared = "£50,000,000"
jackpotamount = "£25,000,000"
twoamount = "£12,532,742"

class MyWindow:
   
    def __init__(self, win):

        self.spinning = False
        self.spinthread = None

        self.lbl1=Label(win, text='1', font=("Arial", 40))
        self.lbl2=Label(win, text='0', font=("Arial", 40))
        self.lbl3=Label(win, text='1', font=("Arial", 40))
        self.lbl4=Label(win, text='', font=("Arial", 25))
        self.lbl1.place(x=100, y=75)
        self.lbl2.place(x=140, y=75)
        self.lbl3.place(x=180, y=75)
        self.lbl4.place(x=50, y=160)
        self.b1=Button(win, text='Start Spinning', command=self.start_spin)
        self.b2=Button(win, text='Stop Spinning', command=self.clik)
        self.b1.place(x=100, y=50)
        self.b2.place(x=100, y=140)

    def start_spin(self):
        if not self.spinning:
            self.spinning = True
            self.spinthread = threading.Thread(target=self.spin)
            self.spinthread.start()

    def spin(self):
        while self.spinning:
            eee = str(random.randrange(100, 999, 1))
            ee = list(eee)
            self.lbl1["text"]=str(ee[0])
            self.lbl2["text"]=str(ee[1])
            self.lbl3["text"]=str(ee[2])
            time.sleep(0.15)



    def clik(self):
        self.spinning = False
        if self.lbl1["text"] == self.lbl2["text"] and self.lbl2["text"] == self.lbl3["text"]:
            winstatement = "You win "+jackpotamount+"! \nTry again to perhaps earn more..?"
            self.lbl4["text"]=winstatement
            print("Win!")
        elif self.lbl1["text"] == self.lbl2["text"] or self.lbl2["text"] == self.lbl3["text"]:
            winstatement = "You win "+twoamount+"! \nTry again to perhaps earn more..?"
            self.lbl4["text"]=winstatement
            print("Win!")
        elif self.lbl1["text"] == 9 and self.lbl2["text"] == 9 and self.lbl3["text"] == 9:
            winstatement = "You win "+jackpotsquared+"! \nTry again to perhaps earn more..?"
            self.lbl4["text"]=winstatement
            print("Win!")
        else:
            self.lbl4["text"]="You lose, try again."

window=Tk()
mywin=MyWindow(window)
window.title('Hello Python - This is a slot machine :=)')
window.geometry("640x480+10+10") #XSIZExYSIZE+XPOS+YPOS
window.mainloop()


exit
