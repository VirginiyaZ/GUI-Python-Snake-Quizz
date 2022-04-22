
import tkinter as tk


def add_digit(digit):
    value=calc_entry.get()
    if value[0]=='0' and len(value)==1:
        value = value[1:]
    calc_entry.delete(0,tk.END)
    calc_entry.insert(0,value+digit)


def add_operation(opt):
    value=calc_entry.get() 
    if value[-1] in '-+/*':
        value=value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value=calc_entry.get()
    calc_entry.delete(0,tk.END)
    calc_entry.insert(0,value+opt)  

    
def calculate():
    value = calc_entry.get()
    if value[-1] in '+-/*':
        value=value+value[:-1]

    calc_entry.delete(0,tk.END)
    calc_entry.insert(0,eval(value))


def clear():
    calc_entry.delete(0,tk.END)
    calc_entry.insert(0,0)



def make_digit_button(digit):
    return tk.Button(text=digit,bd=3, font=('Arial',12), command=lambda:add_digit(digit))


def make_operation_button(opt):
    return tk.Button(text=opt,bd=3, font=('Arial',12), 
    fg='red', command=lambda:add_operation(opt))


def make_calc_button(operation):
    return tk.Button(text=operation,bd=3, font=('Arial',12), 
    fg='red', command=calculate)

def make_clear_button(operation):
    return tk.Button(text=operation,bd=3, font=('Arial',12), 
    fg='red', command=clear)


win = tk.Tk()
win.title('Calculator')
w = win.winfo_screenwidth()
h = win.winfo_screenheight()
w=w//2
h=h//2
w=w-100
h=h-100
win.geometry(f'240x270+{w}+{h}')
# win.geometry('240x260+100+200')
win['bg']='#CFEC85'

calc_entry = tk.Entry(win, justify=tk.RIGHT, font=('Arial',14),width=15)
calc_entry.insert(0,'0')
calc_entry.grid(row=0,column=0, columnspan=4,stick='we', padx=5)

make_digit_button('1').grid(row=1,column=0,stick='wens',padx=2,pady=2)
make_digit_button('2').grid(row=1,column=1,stick='wens',padx=2,pady=2)
make_digit_button('3').grid(row=1,column=2,stick='wens',padx=2,pady=2)
make_digit_button('4').grid(row=2,column=0,stick='wens',padx=2,pady=2)
make_digit_button('5').grid(row=2,column=1,stick='wens',padx=2,pady=2)
make_digit_button('6').grid(row=2,column=2,stick='wens',padx=2,pady=2)
make_digit_button('7').grid(row=3,column=0,stick='wens',padx=2,pady=2)
make_digit_button('8').grid(row=3,column=1,stick='wens',padx=2,pady=2)
make_digit_button('9').grid(row=3,column=2,stick='wens',padx=2,pady=2)
make_digit_button('0').grid(row=4,column=0,stick='wens',padx=2,pady=2)

make_operation_button('+').grid(row=1,column=3,stick='wens',padx=2,pady=2)
make_operation_button('-').grid(row=2,column=3,stick='wens',padx=2,pady=2)
make_operation_button('/').grid(row=3,column=3,stick='wens',padx=2,pady=2)
make_operation_button('*').grid(row=4,column=3,stick='wens',padx=2,pady=2)

make_calc_button('=').grid(row=4,column=2,stick='wens',padx=2,pady=2)

make_clear_button('C').grid(row=4,column=1,stick='wens',padx=2,pady=2)




win.columnconfigure(0,minsize=60)
win.columnconfigure(1,minsize=60)
win.columnconfigure(2,minsize=60)
win.columnconfigure(3,minsize=60)

win.rowconfigure(1,minsize=60)
win.rowconfigure(2,minsize=60)
win.rowconfigure(3,minsize=60)
win.rowconfigure(4,minsize=60)

win.mainloop()