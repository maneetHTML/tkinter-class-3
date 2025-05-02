from tkinter import*
from tkinter import messagebox
root=Tk()
root.title('App')
root.geometry('400x400')
def display ():
    #messagebox.askyesno("Asking yes or no"," hi click yes or no")
    #messagebox.showinfo("Asking yes or no"," hi click yes or no")
    #messagebox.showwarning("Asking yes or no"," hi click yes or no")
    #messagebox.showerror("Asking yes or no"," hi click yes or no")
    #messagebox.askquestion("Asking yes or no"," hi click yes or no")
    #messagebox.askokcancel("Asking yes or no"," hi click yes or no")
    messagebox.askretrycancel("Asking yes or no"," hi click yes or no")
button=Button(root,text="hi click me",command=display)
button.pack()
root.mainloop()