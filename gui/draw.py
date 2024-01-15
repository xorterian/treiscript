# Check syntax, interpret, make svg and draw it.

from . import *

from core.treipreter import treipreter

def syntax(code, level=1):
    """Check syntax."""
    if False:
        # A to-do is here.
        messagebox.showerror('Syntax Error', 'In the given TreiScript code syntax error is detected.')
        return
    return True

# Draw
def draw(frame, entries, ima):
    dx = float(entries['Size'].get())
    print("dx", dx)
    code = str(entries['Bare TreiScript'].get())
    print("TreiScript", code)
    if not syntax(code):
        return
    try:
        d = treipreter(code)
    except:
        messagebox.showerror('Draw-time Error', 'The given TreiScript code could not been interpreted.')
        return
    try:
        d.save_png('tmp/tmp.png')
        ent = tk.Label(frame, borderwidth=0, highlightthickness=0)#, background="white")
        ent.image = PhotoImage(master=frame, file='tmp/tmp.png')
        ima.configure(image=ent.image)
    except:
        messagebox.showerror('Drawing Error', 'The interpreted TreiScript code lead to a damaged image.')
        return
