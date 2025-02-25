
import tkinter as tk
from tkinter import messagebox
#esto sirve para importar las funciones matematicas
import math

def calculate_quadratic():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())

        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            x1 = (-b - math.sqrt(discriminant)) / (2*a)
            x2 = (-b + math.sqrt(discriminant)) / (2*a)
            label_result.config(text=f"x1: {x1}\nx2: {x2}")
            messagebox.showinfo("Si se pudo", f"Input values: a={a}, b={b}, c={c}\nResults: x1={x1}, x2={x2}")
        else:
            label_result.config(text="sorry es negativo")
            #esto muestra el mensaje ese 
           

    except ValueError:
        messagebox.showerror("Q NO SE PUEDE >:|", "PONLO BIEN")

        #en python lo del principio se coloca hasta el final jsjsjs 
root = tk.Tk()
root.title("Formula General")

tk.Label(root, text="a:").grid(row=0, column=0)
tk.Label(root, text="b:").grid(row=1, column=0)
tk.Label(root, text="c:").grid(row=2, column=0)

entry_a = tk.Entry(root)
entry_b = tk.Entry(root)
entry_c = tk.Entry(root)

entry_a.grid(row=0, column=1)
entry_b.grid(row=1, column=1)
entry_c.grid(row=2, column=1)

tk.Button(root, text="picale", command=calculate_quadratic).grid(row=3, column=0, columnspan=2)

label_result = tk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=2)

root.mainloop() #hace que funcione al interactuaer con el usuario 
#no se ´por q no me jala pipipipipip
