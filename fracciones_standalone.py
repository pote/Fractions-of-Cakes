# -*- coding: utf-8 -*-
import gtk
from application import ApplicationManager

class FraccionesStandalone(gtk.Window):
    """ Clase principal cuando se corre por fuera de Sugar """
    def __init__(self):
        super(FraccionesStandalone, self).__init__(gtk.WINDOW_TOPLEVEL)

        # conectar maquina de estados principal
        self.application_manager = ApplicationManager(self)
