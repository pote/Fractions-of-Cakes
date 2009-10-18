# -*- coding: utf-8 -*-
import gtk, pygtk
from util import reparent
from estados import *

pygtk.require("2.0")

class ApplicationManager(object):
    """ Maquina de estados principal

    -Inicializa el contenido exterior de la ventana (marco) tanto para Sugar como Standalone, para ello
     recibe una instancia de gtk.Window como argumento del constructor.
    -Provee el metodo 'change_state' utilizado para cargar un nuevo bloque interior dentro del marco.
    -Provee atributo 'state_info' (diccionario compartido que almacena los datos de cada contenido cargado).
    """
    estados_dict = {
        "Inicio": Inicio,
        "Start": Start,
        "Juego": Juego,
        "Fin": Fin,
    }

    def __init__(self, window):
        super(ApplicationManager, self).__init__()

        builder = reparent(self, "frame.glade", window)
        self.inner_container = builder.get_object("inner_container")

        window.connect("destroy", self.gtk_main_quit)
        window.set_title("Fracciones")

        self.state_info = dict()
        self.change_state("Inicio")

        window.show()


    def change_state(self, new_state):
        new_state_instance = self.estados_dict[new_state](self)
        reparent(new_state_instance, new_state_instance.template, self.inner_container)


    def gtk_main_quit(self, userdata=None):
        gtk.main_quit()
