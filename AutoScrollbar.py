"""

Class written by Fredrik Lundh
Date: August 08, 1998

http://effbot.org/zone/tkinter-autoscrollbar.htm

"""

from tkinter import *

class AutoScrollbar(Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            # self.tk.call("grid", "remove", self)
            self.grid_remove()
        else:
            self.grid()
        Scrollbar.set(self, lo, hi)
    def pack(self, **kw):
        raise TclError("Cannot use pack with this widget")
    def place(self, **kw):
        raise TclError("Cannot use place with this widget")