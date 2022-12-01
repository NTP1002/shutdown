from tkinter import *
from os import *
import os
import tkinter

window = Tk()
window.geometry("600x400")
window.title("타이머")
window.resizable(False, False)

hb = 0
mb = 0
sb = 0

hbc = 0
mbc = 0
sbc = 0

def btnrepress(x):
    os.system(f"shutdown -s -t {x}")

def btnpress():
    hb = ht.get()
    mb = mt.get()
    sb = st.get()
    hbc = int(hb)
    mbc = int(mb)
    sbc = int(sb)
    
    sb = sbc + hbc*3600 + mbc*60
    
    nw = Tk()
    nw.geometry("200x100")
    nw.title("재확인")
    nw.resizable(False,False)
    
    nwl = Label(nw)
    nwl.config(text=str(hbc) + "시간" + str(mbc) + "분" + str(sbc) + "초")
    nwl.pack()
    
    nwbtn = Button(nw)
    nwbtn.config(text="실행")
    nwbtn.config(width=30)
    nwbtn.config(command=btnrepress(sb))
    nwbtn.pack()
    
    nw.mainloop()

ts = Label(window)
ts.config(text="시간: ")
ts.place(x=130,y=80)

ts2 = Label(window)
ts2.config(text="분: ")
ts2.place(x=240,y=80)

ts3 = Label(window)
ts3.config(text="초: ")
ts3.place(x=340,y=80)

tl = Label(window)
tl.config(text="")
tl.place(x=220,y=10)

ht = Entry(window)
ht.insert(0, "0")
ht.config(width=8)
ht.place(x=170,y=80)

mt = Entry(window)
mt.insert(0, "0")
mt.config(width=8)
mt.place(x=270,y=80)

st = Entry(window)
st.insert(0, "0")
st.config(width=8)
st.place(x=370,y=80)

btn = Button(window)
btn.config(text = "실행")
btn.config(width=30)
btn.config(command=btnpress)
btn.place(x=190,y=100)


window.mainloop()
