# -*- coding: utf-8 -*-
import gtk
from os import path

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