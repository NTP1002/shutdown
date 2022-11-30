from tkinter import *
window = Tk()
window.geometry("600x400")
window.title("타이머")
window.resizable(False, False)

hb = 0
mb = 0
sb = 0


def btnpress():
    hb = ht.get()
    mb = mt.get()
    sb = st.get()
    hb *=3600
    mb *=60
    sb = sb+hb+mb
    ts.config(text = sb)

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
ht.config(width=8)
ht.place(x=170,y=80)

mt = Entry(window)
mt.config(width=8)
mt.place(x=270,y=80)

st = Entry(window)
st.config(width=8)
st.place(x=370,y=80)

btn = Button(window)
btn.config(text = "실행")
btn.config(width=30)
btn.config(command=btnpress)
btn.place(x=190,y=100)


window.mainloop()