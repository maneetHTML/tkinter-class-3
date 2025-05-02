from tkinter import*
root=Tk()
root.title('App')
root.geometry('400x400')
def display (event):
    print(event.char)
def fun(event):
    print("Button clicked")
btn=Button(text='Click me ')
btn.pack()
btn.bind('<Button-1>',fun)
root.bind('<Key>',display)
root.mainloop()