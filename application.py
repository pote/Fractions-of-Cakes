# -*- coding: utf-8 -*-
import gtk, pygtk
from os import path

pygtk.require("2.0")

def reparent(manager, template, container):
    # construye en nuevo contenido a partir del template de Glade
    builder = gtk.Builder()
    builder.add_from_file(path.join("templates", template))
    # conecta señales a la clase controladora
    builder.connect_signals(manager)

    # elimina contenido previo si existe
    for child in container.get_children():
        container.remove(child)

    # inserta el nuevo contenido en el viejo contenedor
    window = builder.get_object("window")
    for child in window.get_children():
        child.reparent(container)

    return builder

class Inicio(object):
    template = "inicio.glade"

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
        self.change_state(Inicio)

        window.show()

    def change_state(self, state_class):
        reparent(state_class(), state_class.template, self.inner_container)

    def gtk_main_quit(self, userdata=None):
        gtk.main_quit()
