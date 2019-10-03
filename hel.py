from tkinter import Tk, Frame, BOTH, Menu, TclError, Label, RAISED, SUNKEN, SOLID, messagebox


r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append('<123 "dwada" ²1! dwaAd')
r.update() # now it stays on the clipboard after the window is closed
r.destroy()
