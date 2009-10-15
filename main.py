#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gtk
from fracciones_standalone import FraccionesStandalone

if __name__ == "__main__":
    # crea ventana standalone
    standalone = FraccionesStandalone()
    # loop de eventos
    gtk.main()
