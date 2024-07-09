import tkinter as tk
calculatuion = ""

def add_to_calculation(symbol):
    global calculatuion
    calculatuion +=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculatuion)

def evaluate_calculation():
    global calculatuion
    print(calculatuion)
    try:
        calculatuion = str(eval(calculatuion))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculatuion)
    except:
        clear_filed()
        text_result.insert(1.0,"Error")

def clear_filed():
    global calculatuion
    calculatuion = " "
    text_result.delete(1.0 , "end") 

root =tk.Tk()
root.configure(bg='#17161b')
root.geometry("300x275")

text_result=tk.Text(root,height=2 , width=16 , font=("Arial",24))
text_result.grid(columnspan=5)


btn_1 = tk.Button(root , text="1" ,command=lambda: add_to_calculation(1) , width=5 , font=("Arial",14),bd=1,fg='#fff',bg='#2a2d36')
btn_1.grid(row=4 ,column=1)

btn_2 = tk.Button(root , text="2" ,command=lambda: add_to_calculation(2) , width=5 , font=("Arial",14),bd=1,fg='#fff',bg='#2a2d36')
btn_2.grid(row=4 ,column=2)

btn_3 = tk.Button(root , text="3" ,command=lambda: add_to_calculation(3) , width=5 , font=("Arial",14),bd=1,fg='#fff',bg='#2a2d36')
btn_3.grid(row=4 ,column=3)

btn_4 = tk.Button(root , text="4" ,command=lambda: add_to_calculation(4) , width=5 , font=("Arial",14),bd=1,fg='#fff',bg='#2a2d36')
btn_4.grid(row=3 ,column=1)

btn_5 = tk.Button(root , text="5" ,command=lambda: add_to_calculation(5) , width=5 , font=("Arial",14),bd=1,fg='#fff',bg='#2a2d36')
btn_5.grid(row=3 ,column=2)

btn_6 = tk.Button(root , text="6" ,command=lambda: add_to_calculation(6) , width=5 , font=("Arial",14),bd=1,fg='#fff',bg='#2a2d36')
btn_6.grid(row=3 ,column=3)

btn_7 = tk.Button(root , text="7" ,command=lambda: add_to_calculation(7) , width=5 , font=("Arial",14),bd=1,fg='#fff',bg='#2a2d36')
btn_7.grid(row=2 ,column=1)

btn_8 = tk.Button(root , text="8" ,command=lambda: add_to_calculation(8) , width=5 , font=("Arial",14),bd=1,fg='#fff',bg='#2a2d36')
btn_8.grid(row=2 ,column=2)

btn_9 = tk.Button(root , text="9" ,command=lambda: add_to_calculation(9) , width=5 , font=("Arial",14),bd=1,fg='#fff',bg='#2a2d36')
btn_9.grid(row=2 ,column=3)

btn_0 = tk.Button(root , text="0" ,command=lambda: add_to_calculation(0) , width=5 , font=("Arial",14),bd=1,fg='#fff',bg='#2a2d36')
btn_0.grid(row=5 ,column=2)

btn_plus = tk.Button(root , text="+" ,command=lambda: add_to_calculation("+") , width=5 , font=("Arial",14),bd=1,fg='#fff',bg='#2a2d36')
btn_plus.grid(row=2,column=4)

btn_minus = tk.Button(root , text="-" ,command=lambda: add_to_calculation("-") , width=5 , font=("Arial",14),bd=1,fg='#fff',bg='#2a2d36')
btn_minus.grid(row=1,column=4)

btn_mul = tk.Button(root , text="/" ,command=lambda: add_to_calculation("/") , width=5 , font=("Arial",14),bd=1,fg='#fff',bg='#2a2d36')
btn_mul.grid(row=1,column=2)

btn_div = tk.Button(root , text="*" ,command=lambda: add_to_calculation("*") , width=5 , font=("Arial",14),bd=1,fg='#fff',bg='#2a2d36')
btn_div.grid(row=1,column=3)

btn_open = tk.Button(root , text="(" ,command=lambda: add_to_calculation("(") , width=5 , font=("Arial",14),bd=1,fg='#fff',bg='#2a2d36')
btn_open.grid(row=5,column=1)

btn_close = tk.Button(root , text=")" ,command=lambda: add_to_calculation(")") , width=5 , font=("Arial",14),bd=1,fg='#fff',bg='#2a2d36')
btn_close.grid(row=5,column=3)

btn_clear = tk.Button(root , text="C" ,command=clear_filed , width=5, font=("Arial",14),bd=1,fg='#fff',bg='#3697f5')
btn_clear.grid(row=1,column=1)

btn_equals = tk.Button(root , text="=" ,command=evaluate_calculation , width=5,height=4,font=("Arial",14),bd=1,fg='#fff',bg='#fe9037')
btn_equals.place(x=225,y=150)


root.mainloop()