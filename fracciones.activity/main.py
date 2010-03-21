#!/usr/bin/env python
# -*- coding: utf-8 -*-.
import gtk
from fractionpresentation import FractionPresentation


class FraccionesStandalone(gtk.Window):
    def __init__(self):
        super(FraccionesStandalone, self).__init__() 
        self.add(FractionPresentation())
        self.connect("destroy", gtk.main_quit)
        self.show()
 

if __name__ == "__main__":
    FraccionesStandalone()
    gtk.main()
