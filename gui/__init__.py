# Import each graphics-related module
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from __main__ import dx

folder = 'gui.'
for to_import in ['draw', 'io', 'help', 'viewer']:
  exec('from '+folder+to_import+' import *')
