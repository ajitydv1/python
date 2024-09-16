import tkinter as tk
root=tk.Tk()
#root.geometry('400 x 250')
root.geometry("500x400")
root.title("my window")
text_var=tk.StringVar()
text_var.set("hello,world!")
label=tk.Label(root,
               textvariable=text_var,
               anchor=tk.CENTER,
               bg='pink',
               height=3,
               width=30,
               bd=3,
               font=("arial",16,"bold"),
               cursor="hand2",
               fg="red",
               padx=15,
               pady=15,
               justify=tk.CENTER,
               relief=tk.RAISED,
               underline=0,
               wraplength=50
               )
label.pack(pady=20)
root.mainloop()