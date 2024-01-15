# Build the gui with input fields and buttons.
# Contain also the drawing panel.

from . import *

def makeform(root, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        if field=='Filename':
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
root.title(defs['appname']+' '+defs['vers'])
menubar = Frame()
menubar.pack()
b_saveScr = tk.Button(menubar, text='Save')
b_saveScr.pack(side=tk.LEFT, padx=5, pady=5)
b_openScr = tk.Button(menubar, text='Open')
b_openScr.pack(side=tk.LEFT, padx=5, pady=5)
b_reset = tk.Button(menubar, text='Reset')
b_reset.pack(side=tk.LEFT, padx=5, pady=5)
b_set = tk.Button(menubar, text='Settings', state='disabled')
b_set.configure(state='disabled')
b_set.pack(side=tk.LEFT, padx=5, pady=5)
b_help = tk.Button(menubar, text='Help', command=help_html)
b_help.pack(side=tk.LEFT, padx=5, pady=5)
b_quit = tk.Button(menubar, text='Quit', command=root.quit)
b_quit.pack(side=tk.RIGHT, padx=5, pady=5)

editor = Frame()
editor.pack(side=LEFT)
ents = makeform(editor, defs['fields'])

fr_view = Frame()
fr_view.pack(side=RIGHT, fill="y")

ent = tk.Label(fr_view, borderwidth=0, highlightthickness=0)#, background="white")
ent.image = PhotoImage(master=fr_view, file='tmp/tmp.png')
ima = tk.Label(fr_view, image=ent.image)

b_saveScr.configure(command=(lambda fr=root, e=ents: save_file(fr,e)))
b_openScr.configure(command=(lambda fr=root, fr_view=fr_view, e=ents: open_file(fr,fr_view,ima,e)))
#b_set.configure(command=(lambda fr=root, e=ents: settings(fr,e))) #to-do
b_reset.configure(command=(lambda fr=root, fr_view=fr_view, ima=ima, e=ents: open_file(fr,fr_view,ima,e,True)))

b_draw = tk.Button(fr_view, text='Draw',
       command=(lambda e=ents, ima=ima: draw(fr_view, e, ima)))
b_draw.pack(side=tk.TOP, padx=5, pady=5)
import pyperclip
b_copy = tk.Button(fr_view, text='Copy',
       command=(lambda e=ents: pyperclip.copy(str(e['Bare TreiScript'].get()))))
b_copy.pack(side=tk.TOP, padx=5, pady=5)

ima.pack(side=tk.LEFT, fill="y")

root.mainloop()
