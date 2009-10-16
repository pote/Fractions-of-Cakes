# -*- coding: utf-8 -*-
import gtk, pygtk
from util import reparent
from estados import Inicio

pygtk.require("2.0")

class ApplicationManager(object):
    """ Maquina de estados principal

    -Inicializa el contenido exterior de la ventana (marco) tanto para Sugar como Standalone, para ello
     recibe una instancia de gtk.Window como argumento del constructor.
    -Provee el metodo 'change_state' utilizado para cargar un nuevo bloque interior dentro del marco.
    -Provee atributo 'state_info' (diccionario compartido que almacena los datos de cada contenido cargado).
    """
    def __init__(self, window):
        super(ApplicationManager, self).__init__()

        builder = reparent(self, "frame.glade", window)
        self.inner_container = builder.get_object("inner_container")

        window.connect("destroy", self.gtk_main_quit)
        window.set_title("Fracciones")

        self.state_info = dict()
        self.change_state(Inicio(self))

        window.show()


    def change_state(self, state_class):
        reparent(state_class, state_class.template, self.inner_container)


    def gtk_main_quit(self, userdata=None):
        gtk.main_quit()
