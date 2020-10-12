from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import os
form = Tk()
fnt ='None 30 bold'
bg = '#eeaaff'
bgtxt = '#ffffff'
fg = '#0000ff'
fw = 700
fh = 500
x = (form.winfo_screenwidth() - fw) / 2
y =  (form.winfo_screenheight() - fh) /2 
pad = 10
form.geometry('%dx%d+%d+%d'%(fw,fh,x,y))
form.title('Employee File Data')
form.config(bg=bg)
Label(form,text='Employee Data',bg='navy',fg='lightblue',font=fnt).pack(pady=pad)  #pady =>margin top
frame = Frame(form,bg=bg)
frame.pack(pady=pad)
Label(frame,text='Code:',bg=bg,fg=fg,font=fnt).grid(row=0,column=0)
Label(frame,text='Name:',bg=bg,fg=fg,font=fnt).grid(row=1,column=0)
Label(frame,text='Address:',bg=bg,fg=fg,font=fnt).grid(row=2,column=0)
svcode = StringVar()
svname = StringVar()
svaddress = StringVar()
txtcode = Entry(frame,bg=bgtxt,fg='black',font=fnt,textvariable=svcode)
txtname = Entry(frame,bg=bgtxt,fg='black',font=fnt,textvariable=svname) 
txtaddress = Entry(frame,bg=bgtxt,fg='black',font=fnt,textvariable=svaddress)

txtcode.grid(row=0,column=1,pady=pad)
txtname.grid(row=1,column=1,pady=pad)
txtaddress.grid(row=2,column=1,pady=pad)

def create():
	if svcode.get().strip() == '':   #strip removes the spaces
		messagebox.showinfo('','Code is empty !')
		txtcode.focus() #put the mouse on it
	if svname.get().strip() == '':   #strip removes the spaces
		messagebox.showinfo('','Name is empty !')
		txtname.focus()
	if svaddress.get().strip() == '':   #strip removes the spaces
		messagebox.showinfo('','Address is empty !')
		txtaddress.focus()
	else:
		filename = svcode.get() + '_' + svname.get() + '.txt'
		if os.path.isfile(filename)==True:
			messagebox.showerror('Error','The file of this employee exists already')
		else:
			f=open(filename,'w+')
			f.write('Code: ' + svcode.get()+'\n')
			f.write('Name: ' + svname.get()+'\n')
			f.write('Address: ' + svaddress.get()+'\n')
			f.close()
			svcode.set('')
			svname.set('')
			svaddress.set('')
			messagebox.showinfo('','Employee File Created....')

btns = ttk.Style()
btns.configure('TButton',font=fnt,pady=pad,padding=pad) 
ttk.Button(form,text='Create Employee File Now',command=create).pack(pady=pad)
ttk.Button(form,text='Exit Now',command=form.destroy).pack(pady=pad)
form.mainloop()  