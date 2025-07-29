# import tkinter as tk
# root = tk.Tk()
# root.title("My First GUI")
# root.geometry("400x300")
# root.mainloop()

#button +label
import tkinter as tk
# def greet():
#                label.config(text = "hello,Tkinter!")

# root = tk.Tk()
# root.title("Grret App")
# root.geometry("300x150")
# label = tk.Label(root,text = "Click the button !",font = ("Arial",14))
# label.pack(pady = 10)
# btn = tk.Button(root,text = "Greet",command = greet)
# btn.pack()
# root.mainloop()



#entry box user
def show_nm():
               name = entry.get()
               label.config(text = f" Hello,{name}!")
root = tk.Tk()
root.title ("Name App")
root.geometry("300x150")
entry = tk.Entry(root)
entry.pack(pady = 10)

btn = tk.Button(root,text = "submit",command=show_nm)
btn.pack()
label = tk.Label(root,text = " ")
label.pack()
root.mainloop()


