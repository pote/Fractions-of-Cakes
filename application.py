# -*- coding: utf-8 -*-
import gtk, pygtk
from os import path

pygtk.require("2.0")

def reparent(manager, template, container):
    builder = gtk.Builder()
    builder.add_from_file(path.join("templates", template))
    builder.connect_signals(manager)

    window = builder.get_object("window")
    for child in window.get_children():
        child.reparent(container)

class ApplicationManager(object):
    """ Maquina de estados principal

    -Inicializa contenido de la ventana (marco) tanto para Sugar como Standalone
    -Provee el metodo 'change_state' utilizado para cargar un nuevo bloque dentro del marco
    -Provee atributo 'state_info' (diccionario compartido que almacena los datos de cada contenido cargado)
    """
    def __init__(self, frame_container):
        super(ApplicationManager, self).__init__()

        reparent(self, "frame.glade", frame_container)

        #self.state_info = dict()
        #self.change_state(Inicio(self))

        frame_container.connect("destroy", self.gtk_main_quit)
        frame_container.show()

    def gtk_main_quit(self, userdata=None):
        gtk.main_quit()
