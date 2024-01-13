# 

from . import *

from tkinter import *
from tkinter import ttk

import tkinter as tk

from tkinter.filedialog import askopenfilename, asksaveasfilename

from core.treipreter import treipreter

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def syntax():
    """Check syntax."""
    
'''
def draw(code):
    """Draw formula."""
    print(code)
    d = treipreter(code)
    d.save_png('tmp/tmp.png')
    img1 = PhotoImage(master=window, file='tmp/tmp.png')
    lbl_view = tk.Label(master=window, image=img1)

def evaluate(event):
    res.configure(text = "Result: " + str(eval(entry.get())))

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"

def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"


window = tk.Tk()

window.rowconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)
# 0: nav bar
# 1: style setups
# 2: script editor
# 3: viewer
# 4: error message
window.columnconfigure([0, 1, 2, 3, 4], minsize=100, weight=1)
# 0/0: Save script, 0/1: Open script, 0/2: Settings, 0/3: help, 0/4: save ima
# 1/0..3: dx, syntax checker,
# 2/0: text field, draw button
# 3: image

window.title("Simple Text Editor")
'''

import tkinter as tk

fields = ('Bare TreiScript', 'High-level script', 'File name', 'Size', 'Padding')

# Draw
def draw(frame, entries, ima):
    dx = float(entries['Size'].get())
    print("dx", dx)
    code = str(entries['Bare TreiScript'].get())
    print("TreiScript", code)
    d = treipreter(code)
    d.save_png('tmp/tmp.png')
    ent = tk.Label(frame, borderwidth=0, highlightthickness=0)#, background="white")
    ent.image = PhotoImage(master=frame, file='tmp/tmp.png')
    ima.configure(image=ent.image)
    
def makeform(root, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        if field=='File name':
            ent.insert(0, "Untitled")
        elif field=='Size':
            ent.insert(0, "32")
        else:
            ent.insert(0, "0")
        if field in ['High-level script','Size']:
            ent.configure(state='disabled')
        row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, 
                 expand=tk.YES, 
                 fill=tk.X)
        entries[field] = ent
    return entries

root = tk.Tk()
root.title("TreiScript - Editor - (beta v0.1)")
menubar = Frame()
menubar.pack()
b_saveScr = tk.Button(menubar, text='Save', command=(lambda _=0: print('Save')))
b_saveScr.pack(side=tk.LEFT, padx=5, pady=5)
b_openScr = tk.Button(menubar, text='Open', command=(lambda _=0: print('Open')))
b_openScr.pack(side=tk.LEFT, padx=5, pady=5)
b_reset = tk.Button(menubar, text='Reset', command=(lambda _=0: print('Reset')))
b_reset.pack(side=tk.LEFT, padx=5, pady=5)
b_set = tk.Button(menubar, text='Settings', command=(lambda _=0: print('Settings...')))
b_set.configure(state='disabled')
b_set.pack(side=tk.LEFT, padx=5, pady=5)
b_help = tk.Button(menubar, text='Help', command=(lambda _=0: print('Help')))
b_help.pack(side=tk.LEFT, padx=5, pady=5)
b_quit = tk.Button(menubar, text='Quit', command=root.quit)
b_quit.pack(side=tk.RIGHT, padx=5, pady=5)

editor = Frame()
editor.pack(side=LEFT)
ents = makeform(editor, fields)

fr_view = Frame()
fr_view.pack(side=RIGHT, fill="y")

ent = tk.Label(fr_view, borderwidth=0, highlightthickness=0)#, background="white")
ent.image = PhotoImage(master=fr_view, file='tmp/tmp.png')
ima = tk.Label(fr_view, image=ent.image)
b_draw = tk.Button(fr_view, text='Draw',
       command=(lambda e=ents, ima=ima: draw(fr_view, e, ima)))
b_draw.pack(side=tk.TOP, padx=5, pady=5)

ima.pack(side=tk.LEFT, fill="y")

root.mainloop()
