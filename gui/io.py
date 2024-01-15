# I/O and reset method.

from . import *

from tkinter.filedialog import askopenfilename, asksaveasfilename
from core.treipreter import treipreter
import xml.etree.ElementTree as ET

def reset(frame=0, frame_view=0, ima=0, ents=0):
    global defs
    global xml
    defs = {\
        'appname': 'TreiScript Editor', \
        'vers': 'v0.1 (beta)', \
        'fields': ('Bare TreiScript', 'High-level script', 'Filename', 'Size', 'Padding'), \
        'def_field_values': ('d_var_x', '', 'Untitled', 32, 0), \
        'disabled_fields': ('High-level script', 'Size'), \
        'ext': '.3.xml', \
        'channels': {'colors': ['black']} \
    }
    open_file(frame,frame_view,ima,ents,True)

def save_file(frame,ents):
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension = ".3.xml",
        filetypes = [("TreiScript Files", defs['ext']), ("All XML Files", "*.xml")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        code = str(ents['Bare TreiScript'].get())
        xml[4][1][0].text = code
        output_file.write(ET.tostring(xml, encoding='unicode'))
    frame.title(defs['appname']+' - '+filepath.split('/')[-1].split('\\')[-1])

def open_file(frame, fr_view, ima, ents, reset=False):
    """Open a file for editing."""
    if reset:
        global xml
        filepath = 'assets/template.3.xml'
    else:
        filepath = askopenfilename(
            defaultextension = ".3.xml",
            filetypes = [("TreiScript Files", defs['ext']), ("All XML Files", "*.xml")]
        )
    if not filepath:
        return
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        fname = filepath.\
            split('/')[-1].\
            split('\\')[-1].\
            split('.')[0]
        xml = ET.fromstring(input_file.read())
        code = xml[4][1][0].text
        dx = 32
        defs['vers'] = 'v'+ xml[2].text +  (' ('+ xml[2].attrib['type'] + ')' if 'type' in xml[2].attrib else '')
        defs['title'] = xml[3].text
        
        if frame and ents:
            ents['Bare TreiScript'].delete(0, tk.END)
            ents['Bare TreiScript'].insert(0, code)
            ents['Filename'].delete(0, tk.END)
            ents['Filename'].insert(0, fname)
            ents['Size'].delete(0, tk.END)
            ents['Size'].insert(0, dx)
    if frame and ents:
        frame.title(defs['appname']+(' - '+fname if fname else ''))
        draw(fr_view,ents,ima)

reset()
