# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 16:56:21 2021

@author: Dipanjan
"""
from tkinter import*
from tkinter.filedialog import asksaveasfilename 
from tkinter.filedialog import askopenfilename
import subprocess

compiler=Tk()
compiler.title("Dipanjan's IDE")
file_path=''

def setfp(path):
    global file_path
    file_path=path

def save_as():
    if file_path=='':
        path=asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path=file_path
    with open(path,'w') as file:
        code=editor.get('1.0',END)
        file.write(code)
        setfp(path)
        
def open_file():
    path=askopenfilename(filetypes=[('Python Files','*.py')])
    with open(path,'r') as file:
        code=file.read()
        editor.delete('1.0',END)
        editor.insert('1.0',code)
        setfp(path)


def run():
    if file_path=='':
        save_prompt=Toplevel()
        text=Label(save_prompt,text="Save Your Code")
        text.pack()	
        return
    command=f'python {file_path}'
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error= process.communicate()
    code_op.insert('1.0', output)
    code_op.insert('1.0', error)

menu_bar=Menu(compiler)

file_bar=Menu(menu_bar,tearoff=0)
file_bar.add_command(label='Open', command=open_file)
file_bar.add_command(label='Save', command=save_as)
file_bar.add_command(label='Save As', command=save_as)
menu_bar.add_cascade(label='File',menu=file_bar)

run_bar=Menu(menu_bar,tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run',menu=run_bar)

compiler.config(menu=menu_bar)

editor=Text()
editor.pack()

code_op=Text(height=12)
code_op.pack()

compiler.mainloop()



