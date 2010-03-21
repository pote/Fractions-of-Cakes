#!/usr/bin/env python
# -*- coding: utf-8 -*-.
#Test Comment

import logging
import gtk
from fracciones_standalone import FraccionesStandalone


logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    # crea ventana standalone
    standalone = FraccionesStandalone()
    # loop de eventos
    gtk.main()
